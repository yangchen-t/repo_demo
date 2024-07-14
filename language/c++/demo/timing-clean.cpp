#include <iostream>
#include <experimental/filesystem>
#include <vector>
#include <string>
#include <chrono>
#include <ctime>
#include <sys/stat.h>
#include <map>
#include <sys/statvfs.h>
#include <iomanip>

namespace fs = std::experimental::filesystem;

enum class Level {
    Low = 0,
    Middle = 1,
    High = 2,
};

struct PathInfo {
    std::string _path;
    float _size;
    Level _level;
};

std::map<std::string, int> creationTime;
std::vector<PathInfo> v;
std::multimap<int, std::string> multiMap;

const int THRESHOLD = 200;

void init();
std::map<std::string, int> getCreateTime(const std::string&, const std::string&);
void findPath(std::string);
double directorySizeCount(const fs::path&);
void convert();
int currentFreeSpace();
void handle();
void deleteUselessFileReleaseSpace(std::vector<PathInfo>::iterator&);

int main() {
    init();
    if (currentFreeSpace() < THRESHOLD){
        std::cout << "sos" << std::endl;
        handle();
    }
    return 0; 
}

void init() {

    PathInfo csv = {"/data/code/all_ws/ws/csv/", 250 , Level::High};
    PathInfo igv_log = {"/data/code/all_ws/ws/igv_log/", 50 , Level::Middle};
    PathInfo coredump = {"/data/code/all_ws/ws/coredump/", 50 , Level::Low};
    PathInfo odom = {"/data/key_log/odom/", 50 , Level::Middle};
    PathInfo logpush_nas = {"/data/code/all_ws/ws/logpush_nas/", 20, Level::Low};
    PathInfo qfile = {"/data/code/all_ws/ws/qfile/", 300, Level::High};
    PathInfo logpush_tmp = {"/data/code/all_ws/ws/logpush_tmp/", 20, Level::Low};
    PathInfo pcd = {"/data/key_log/lidar", 30, Level::Middle};
    PathInfo pcd_int16 = {"/data/key_log/lidar_int16", 30, Level::Middle};
    v.push_back(csv);
    v.push_back(igv_log);
    v.push_back(coredump);
    v.push_back(odom);
    v.push_back(logpush_nas);
    v.push_back(qfile);
    v.push_back(logpush_tmp);
}

void findPath(std::string directory) {
    fs::path directoryPath = directory + "/";

    if (fs::exists(directoryPath) && fs::is_directory(directoryPath)) {
        for (const auto& entry : fs::directory_iterator(directoryPath)) {
            if (fs::is_regular_file(entry.path())) {
                std::map<std::string, int> ret = getCreateTime(directoryPath,  entry.path().filename());
            }else{
                findPath(entry.path());
            }
        }
    } else {
        std::cout << "指定的目录不存在或不是一个有效的目录。" << std::endl;
    }
}

std::map<std::string, int> getCreateTime(const std::string& directoryPath, const std::string& filename) {
    std::string filepath = directoryPath + filename;
    struct stat stat_buffer;
    if (fs::exists(filepath)) {
        int result = stat(filepath.c_str(), &stat_buffer);

        if (result == 0) { // st_atime: Access_time, st_mtime: modify_time st_ctime change_time 
            time_t c_time = stat_buffer.st_mtime; 
            creationTime[filepath] = c_time;
        }else {
            std::cout << filepath << " is stat get err" << std::endl;
        }
        return creationTime;
    }else {
        std::cout << "File does not exist: " << filepath << std::endl;
        return creationTime;
    }
}


double directorySizeCount(const fs::path& folderPath) {
    uintmax_t size = 0;
    double sizeGB = 0;
    for (const auto& p : fs::recursive_directory_iterator(folderPath)) {
        if (!fs::is_directory(p.status())) {
            size += fs::file_size(p);
        }
    }
    if (fs::exists(folderPath) && fs::is_directory(folderPath)) {
        sizeGB = static_cast<double>(size) / (1 << 30); // 转换为 GB
        std::cout << "size: " << std::fixed << std::setprecision(2) << sizeGB << std::endl;
    } else {
        std::cerr << "Invalid folder path." << std::endl;
    }
    return sizeGB;
}

void convert(){
    // 将原始 map 的数据填充到 multimap 中
    for(const auto& pair : creationTime) {
        multiMap.insert(std::make_pair(pair.second, pair.first));
    }
    // 输出按值排序后的结果
    for (const auto& pair : multiMap) {
        std::cout << "Key: " << pair.second << ", Value: " << pair.first << std::endl;
    }
}
int currentFreeSpace(){
    struct statvfs buffer;
    if (statvfs("/data", &buffer) == 0) {
        return buffer.f_bavail * buffer.f_frsize / (1 << 30);
    }else{
        return -1;
    }
}
void handle(){
    for (std::vector<PathInfo>::iterator it = v.begin(); it < v.end(); it++) {
        if (fs::exists(it->_path) && fs::is_directory(it->_path)){
            if (directorySizeCount(it->_path) > it->_size){
                std::cout  << it->_path << std::endl;
                findPath(it->_path);
                convert();
                deleteUselessFileReleaseSpace(it);
            }else {
                std::cout << it->_path << " -> " << it->_size << std::endl;
            }
        }
    }
}

void deleteUselessFileReleaseSpace(std::vector<PathInfo>::iterator& _v){
    for (const auto& pair : multiMap) {
        if (directorySizeCount(_v->_path) < _v->_size){break;}
        else {
            std::cout << pair.second << std::endl;
            fs::remove(pair.second);
        }
    }
}