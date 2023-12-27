#include <chrono>
#include <cstdint>
#include <iostream>
#include <string>
#include <cstring>
#include <libssh/libssh.h>
#include <boost/type_index.hpp>

// #define sIp "192.168.103.120"
#define sPort "22"
#define sHost "westwell"
#define sPasswd " "

struct Offset
{
    std::int64_t time;
    std::int64_t offset;
};

Offset sshOffset;

std::string& bufferToString(char* buffer, int bufflen, std::string& str)
{
    char temp[bufflen];
    memset(temp, '\0', bufflen + 1);
    strncpy(temp, buffer, bufflen);
    return(str.assign(temp));
}

std::int64_t getTimestampUs() {
    auto now = std::chrono::high_resolution_clock::now();
    auto duration = now.time_since_epoch();
    return std::chrono::duration_cast<std::chrono::microseconds>(duration).count();
}

Offset ssh(const char *ip)
{
    std::int64_t start = getTimestampUs();
    ssh_session session = ssh_new();

    // std::cout << boost::typeindex::type_id_with_cvr<decltype(xx)>().pretty_name() << std::endl;
    // 设置服务器地址和端口号
    ssh_options_set(session, SSH_OPTIONS_HOST, ip);
    ssh_options_set(session, SSH_OPTIONS_PORT_STR, sPort);

    // 连接服务器
    int result = ssh_connect(session);
    if (result != SSH_OK)
    {
        std::cerr << "Error: " << ssh_get_error(session) << std::endl;
    }

    // 认证
    result = ssh_userauth_password(session, sHost, sPasswd);
    if (result != SSH_AUTH_SUCCESS)
    {
        std::cerr << "Error: " << ssh_get_error(session) << std::endl;
    }

    // 执行命令
    ssh_channel channel = ssh_channel_new(session);
    ssh_channel_open_session(channel);
    ssh_channel_request_exec(channel,"date '+%s%6N'");

    // 读取命令的输出
    char buffer[1024];
    std::string str;
    int n = ssh_channel_read(channel, buffer, sizeof(buffer), 0);
    while (n > 0)
    {
        std::cout.write(buffer, n);
        n = ssh_channel_read(channel, buffer, sizeof(buffer), 0); 
    }
    // 关闭连接
    ssh_channel_close(channel);
    ssh_disconnect(session);
    ssh_free(session);
    bufferToString(buffer, sizeof(buffer), str);
    std::int64_t end = getTimestampUs();
    sshOffset.time = std::stol(str);
    sshOffset.offset = end - start;
    return sshOffset;
}

int main(int argc, char * argv[]) {
    if (argv[1] == nullptr) {
        std::cout << "needs args" << std::endl;
        return -1;
    }
    const char *ip = argv[1];
    // 程序开始的时间戳
    std::int64_t timestamp = getTimestampUs();
    // 目标主机的时间戳
    Offset ret =  ssh(ip);
    // 目标主机与当前主机的时间差值  目标主机时间 -> 当前主机时间 us
    std::cout << "time offset -> " << (ret.time - (timestamp + ret.offset))  << std::endl;
    return 0;
}