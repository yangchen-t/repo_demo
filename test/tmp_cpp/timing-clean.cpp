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
#include <yaml-cpp/yaml.h>
#include <unistd.h>
#include <algorithm>

namespace fs = std::experimental::filesystem;

enum Level {
    Low ,
    Middle ,
    High,
};

struct PathInfo {
    std::string _path;
    std::string _name;
    float _size;
    Level _level;
};

std::map<std::string, int> creationTime;
std::vector<PathInfo> v;
std::multimap<int, std::string> multiMap;

const std::string CONFIG="config.yaml";

std::map<std::string, int> getCreateTime(const std::string&, const std::string&);
void findPath(std::string);
bool isSpecialFileType(const fs::path&);
long double directorySizeCount(const fs::path&);
void convert();
int currentFreeSpace();
void deleteUselessFileToSize(std::vector<PathInfo>::iterator&,const int);
int timeTransform(int);
void deleteUselessFileByTimeStamp(std::vector<PathInfo>::iterator&, int, const int);
bool compareByLevel(const PathInfo&, const PathInfo&);
inline int autoClean(const int, const int);

int main() {
    if (!fs::exists(CONFIG)) {
        std::cout << "config is not exist, please check " << CONFIG << std::endl;
        return 0;
    }
    while (true){  
        const YAML::Node config = YAML::LoadFile(CONFIG);
        const int THRESHOLD = config["config"]["standard"].as<int>();
        const int DAY = config["config"]["day"].as<int>(); 
        if (currentFreeSpace() < THRESHOLD){
            std::cout << "sos" << std::endl;
            sleep(config["config"]["trigger_time"].as<int>());
            if (config["config"]) {
                const YAML::Node& config_node = config["config"];
                for (const auto& entry : config_node) {
                    std::string directory_name = entry.first.as<std::string>();
                    if (entry.second.IsMap()) {
                        const YAML::Node& subdirectory_node = entry.second;
                        PathInfo subName;
                        subName._path = subdirectory_node["path"].as<std::string>();
                        subName._size = subdirectory_node["size"].as<float>();
                        subName._name = directory_name;
                        
                        // 通过 "level" 键来获取节点的 Level 值
                        if (subdirectory_node["level"]) {
                            int level_str = subdirectory_node["level"].as<int>();
                            if (level_str == Level::Low) {
                                subName._level = Low;
                            } else if (level_str == Level::Middle) {
                                subName._level = Middle;
                            } else if (level_str == Level::High) {
                                subName._level = High;
                            }else{subName._level = Level::Low;}
                        }
                        v.push_back(subName);
                    }
                }
            } autoClean(THRESHOLD, DAY); 
        } v.clear();
    } return 0; 
}

void findPath(std::string _directory) {
    fs::path directoryPath = _directory + "/";

    if (fs::exists(directoryPath) && fs::is_directory(directoryPath)) {
        for (const auto& entry : fs::directory_iterator(directoryPath)) {
            if (fs::is_regular_file(entry.path())) {
                std::map<std::string, int> ret = getCreateTime(directoryPath,  entry.path().filename());
            }else{
                findPath(entry.path());
            }
        }
    } else {
        std::cout << "dir err" << std::endl;
    }
}

std::map<std::string, int> getCreateTime(const std::string& _directoryPath, const std::string& _filename) {
    std::string filepath = _directoryPath + _filename;
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

bool isSpecialFileType(const fs::path& _filePath) {
    // 可以根据需要定义特殊文件类型的判断条件，比如设备文件等
    // 这里简单地假设所有名称以 "." 开头的文件为特殊文件（包括隐藏文件）
    return _filePath.filename().string().front() == '.';
}

long double directorySizeCount(const fs::path& _folderPath) {
    uintmax_t size = 0;
    long double sizeGB = 0;

    for (const auto& p : fs::recursive_directory_iterator(_folderPath)) {
        if (!fs::is_directory(p.status()) && !fs::is_symlink(p)) { // 排除目录和符号链接
            if (!isSpecialFileType(p.path())) { // 忽略特殊文件类型
                size += fs::file_size(p);
            }
        }
    }
    if (fs::exists(_folderPath) && fs::is_directory(_folderPath)) {
        sizeGB = static_cast<long double>(size) / (1 << 30); // 转换为 GB
        std::cout << std::fixed << std::setprecision(2) << sizeGB << "GB ";
    } else {
        std::cerr << "Invalid folder path." << std::endl;
    }
    return sizeGB;
}
void convert(){
    // HACK 时间复杂度上来看，排序算法的O(N log N)比遍历和插入的O(N)效率更高 
    // 将原始 map 的数据填充到 multimap 中 
    for(const auto& pair : creationTime) {
        multiMap.insert(std::make_pair(pair.second, pair.first));
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

int timeTransform(int _day){
    time_t currentTime = time(&currentTime);
    return currentTime - (_day * 60*60*24);
}

// 释放配置文件中大于size空间的额外的文件
void deleteUselessFileBySize(std::vector<PathInfo>::iterator& _v, const int _thershold){
    for (const auto& pair : multiMap) {
        if (currentFreeSpace() <= _thershold){
            if (directorySizeCount(_v->_path) < _v->_size){break;}
            else {
                std::cout << " [S]clean -> " << pair.second << std::endl;
                fs::remove(pair.second);
            }
        }else {std::cout << currentFreeSpace() << std::endl;return;}
    }
}

// 释放标准时间之外的文件
void deleteUselessFileByTimeStamp(std::vector<PathInfo>::iterator& _v, int _timeStamp, const int _thershold){
    for (const auto& pair : multiMap) {
        if (currentFreeSpace() <= _thershold){
            if (directorySizeCount(_v->_path) < _v->_size){return;}
            else{
                if (pair.first < _timeStamp){
                    std::cout << " [T]clean -> " << pair.second << std::endl;
                    fs::remove(pair.second);
                }
            }
        }else {std::cout << currentFreeSpace() << std::endl;return;}
    }
}

bool compareByLevel(const PathInfo& _a, const PathInfo& _b) {
    return _a._level < _b._level;
}

// 当剩余空间 < 规定空间开始按照配置文件中level从低到高的规律逐步释放空间只到大于规定空间后停止
inline int autoClean(const int _thershold, const int _day){
    std::sort(v.begin(), v.end(), compareByLevel);
    // release day filename 
    int standardTime = timeTransform(_day);
    for (std::vector<PathInfo>::iterator it = v.begin(); it < v.end(); it++) {
        if (currentFreeSpace() <= _thershold){
            if (fs::exists(it->_path) && fs::is_directory(it->_path)){
                if (directorySizeCount(it->_path) > it->_size){
                    findPath(it->_path);
                    convert();
                    deleteUselessFileByTimeStamp(it, standardTime, _thershold);
                }else {
                    std::cout << it->_path << " Time -> " << it->_size << std::endl;    
                }
            }
        }else {break;}
    }
    if (currentFreeSpace() > _thershold){
        std::cout << "release time rules useless file, cur space > standard" << std::endl;
        return 0;
    }
    for (std::vector<PathInfo>::iterator it = v.begin(); it < v.end(); it++) {
        if (currentFreeSpace() < _thershold){
            if (fs::exists(it->_path) && fs::is_directory(it->_path)){
                if (directorySizeCount(it->_path) > it->_size){
                    findPath(it->_path);
                    convert();
                    deleteUselessFileBySize(it, _thershold);
                }else {
                    std::cout << it->_path << " Size -> " << it->_size << std::endl;    
                }
            }
        }else{break;}
    }
    return 0;
}