#include <iostream>
#include <filesystem>
#include <vector>
#include <string>
#include <chrono>
#include <ctime>
#include <sys/stat.h>
#include <map>
#include <sys/statvfs.h>

namespace fs = std::filesystem;

enum class Level {
    Low = 0,
    Middle = 1,
    High = 2,
};

struct PathInfo {
    std::string _path;
    int _size;
    Level _level;
};
std::map<std::string, int> creationTime;
const int THRESHOLD = 200;

void init();
std::map<std::string, int> getCreateTime(const std::string&, const std::string&);
void findPath(std::string);
double directorySizeCount(const fs::path&);
void convert();
int currentFreeSpace();
void handle();

int main() {
    init();
    handle();
    if (currentFreeSpace() < THRESHOLD){
        std::cout << "sos" << std::endl;
    }
    convert();
    return 0; 
}

void init() {

    PathInfo csv = {"/data/code/all_ws/ws/csv/", 100 , Level::High};
    PathInfo igv_log = {"/data/code/all_ws/ws/igv_log/", 100 , Level::Middle};
    PathInfo coredump = {"/data/code/all_ws/ws/coredump/", 100 , Level::Low};
    PathInfo odom = {"/data/key_log/odom/", 100 , Level::Middle};
    PathInfo test = {"/debug/igv_log/", 100, Level::Low};
    std::vector<PathInfo> v;
    v.push_back(csv);
    v.push_back(igv_log);
    v.push_back(coredump);
    v.push_back(odom);
    v.push_back(test);

    for (std::vector<PathInfo>::iterator it = v.begin(); it < v.end(); it++) {
        findPath(it->_path);
    }
}

void findPath(std::string directory) {
    fs::path directoryPath = directory;

    if (fs::exists(directoryPath) && fs::is_directory(directoryPath)) {
        directorySizeCount(directory);
        for (const auto& entry : fs::directory_iterator(directoryPath)) {
            if (fs::is_regular_file(entry.path())) {
                std::map<std::string, int> ret = getCreateTime(directory,  entry.path().filename());
            }
        }
    } else {
        std::cout << "指定的目录不存在或不是一个有效的目录。" << std::endl;
    }
}

std::map<std::string, int> getCreateTime(const std::string& directoryPath, const std::string& filename) {
    std::string filepath = directoryPath + filename;
    if (fs::exists(filepath)) {
        struct stat stat_buffer;
        int result = stat(filepath.c_str(), &stat_buffer);

        if (result == 0) {
            time_t c_time = stat_buffer.st_ctime; // last modify time
            creationTime[filepath] = c_time;
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
        std::cout << "Folder size: " << std::fixed << std::setprecision(2) << sizeGB << " GB" << std::endl;
    } else {
        std::cerr << "Invalid folder path." << std::endl;
    }
    return sizeGB;
}

void convert(){
    std::multimap<int, std::string> multiMap;
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

}