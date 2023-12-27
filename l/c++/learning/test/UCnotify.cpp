#include <iostream>
#include <cstring>
#include <cerrno>
#include <cstdio>
#include <pthread.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>

#include "UCInotify.h"
#include "Tools/logTools.h"

using namespace std;

UCInotify::UCInotify(void):m_inotifyFD(0),m_isContinue(true),m_pParameter(NULL)
{
}

UCInotify::~UCInotify(void)
{
}

//初始话监控文件列表
size_t UCInotify::InitWatchFile(std::vector<std::string> &watch_name, void *par, const uint32_t mask /*= IN_ALL_EVENTS*/)
{
    m_inotifyFD = inotify_init(); //创建 initify 实例
    if(m_inotifyFD == -1)
    {
        TRACE(1, "initalize inotify failed.");
        return -1;
    }

    //初始化回调函数集
    m_handleMap[_IGNORED_EVENT] = eventUnmount;
    m_handleMap[_ATTRIB_EVENT]  = eventUnmount;
    m_pParameter = par;

    return AddWatchFile(watch_name, mask);
}

//添加监控文件
int UCInotify::AddWatchFile(std::vector<std::string> &watch_name, const uint32_t mask /*= IN_ALL_EVENTS*/)
{
    vector<string>::iterator it = watch_name.begin();
    int wd;
    while(it != watch_name.end())
    {
        string file_buf = *it++;
        wd = inotify_add_watch(m_inotifyFD, file_buf.c_str(), mask);
        if(wd == -1)
        {
            TRACE(1, "add watch failed.");
            return -1;
        }
        m_watchFiles[wd] = file_buf;
    }
    m_watchNum = m_watchFiles.size();

    return m_watchNum;
}

//删除监控文件
int UCInotify::RmWatchFile(const std::string &rm_file)
{
    int wd = findWD(rm_file);

    return inotify_rm_watch(m_inotifyFD, wd);
}

//开始监控
int UCInotify::StartWatchThread(std::map<string, EventHandle> &func, pthread_t &_pid)
{
    map<string, EventHandle>::iterator it = func.begin();
    while(it != func.end())
    {
        m_handleMap[it->first] = it->second;
        it++;
    }

    _pid = 0;
    return pthread_create(&_pid, NULL, watch_file, (void*)this); //启动监控线程
}

//监控线程
void *UCInotify::watch_file(void *self)
{
    UCInotify *pUCI = (UCInotify*)self;
    ssize_t numRead;

    while(pUCI->m_isContinue)
    {
        //申请特点大小的缓存
        char buf[pUCI->m_watchNum * A_FILE_SIZE];
        bzero(buf, sizeof(buf));
        numRead = read(pUCI->m_inotifyFD, buf, sizeof(buf));
        if(numRead < 0)
        {
            TRACE(1, "Read inotify failed. what: " << strerror(errno));
            return NULL;
        }
        char *p = NULL;
        struct inotify_event *event = NULL;
        for(p = buf; p < (buf + numRead); )
        {
            event = (struct inotify_event*)p;

            string whatEvent, eventName, watchFile;
            pUCI->judgeEventStr(event->mask, whatEvent); //获取时间名称
            pUCI->judgeEventName(event->mask, eventName); //获取时间名称
            //获取文件名称
            watchFile = pUCI->m_watchFiles[event->wd];
            TRACE(6, "The event is: " << eventName << " the file is: " << watchFile);
            if(pUCI->m_handleMap.find(eventName) != pUCI->m_handleMap.end())
            {
                TRACE(6, "The event have handle is: " << eventName << " the file is: " << watchFile);
                if((strcmp(eventName.c_str(), _IGNORED_EVENT) == 0) ||
                    strcmp(eventName.c_str(), _ATTRIB_EVENT) == 0)
                {
                    pUCI->m_handleMap[eventName](watchFile, pUCI); //监控对象自己定义的回调函数
                }
                else
                {
                    pUCI->m_handleMap[eventName](watchFile, pUCI->m_pParameter); //用户提供的回调函数
                }
            }

            p += sizeof(struct inotify_event) + event->len;
        }
    }

    return NULL;
}

//识别事件
void UCInotify::judgeEventStr(uint32_t mask, std::string &event)
{
    if(mask & IN_ACCESS)        event = "File access";
    if(mask & IN_ATTRIB)        event = "The file metadata is modified.";
    if(mask & IN_CLOSE_WRITE)   event = "Close the file open for writing.";
    if(mask & IN_CLOSE_NOWRITE) event = "Close the opened the file read-only.";
    if(mask & IN_CREATE)        event = "Create a file or directory.";
    if(mask & IN_DELETE_SELF)   event = "Delete a file or directory.";
    if(mask & IN_MODIFY)        event = "The file was modified.";
    if(mask & IN_MOVE_SELF)     event = "Move the monitored directory or file itself.";
    if(mask & IN_MOVED_FROM)    event = "File moved outside of the monitored directory.";
    if(mask & IN_MOVED_TO)      event = "File moved to of the monitored directory.";
    if(mask & IN_OPEN)          event = "The file has been opened.";
    if(mask & IN_IGNORED)       event = "Monitored item is unload.";
    if(mask & IN_ISDIR)         event = "The name is directory.";
    if(mask & IN_UNMOUNT)       event = "Target file unload.";
}

void UCInotify::judgeEventName(uint32_t mask, std::string &event)
{
    if(mask & IN_ACCESS)        event = "IN_ACCESS";
    if(mask & IN_ATTRIB)        event = "IN_ATTRIB";
    if(mask & IN_CLOSE_WRITE)   event = "IN_CLOSE_WRITE";
    if(mask & IN_CLOSE_NOWRITE) event = "IN_CLOSE_NOWRITE";
    if(mask & IN_CREATE)        event = "IN_CREATE";
    if(mask & IN_DELETE_SELF)   event = "IN_DELETE_SELF";
    if(mask & IN_MODIFY)        event = "IN_MODIFY";
    if(mask & IN_MOVE_SELF)     event = "IN_MOVE_SELF";
    if(mask & IN_MOVED_FROM)    event = "IN_MOVED_FROM";
    if(mask & IN_MOVED_TO)      event = "IN_MOVED_TO";
    if(mask & IN_OPEN)          event = "IN_OPEN";
    if(mask & IN_IGNORED)       event = "IN_IGNORED";
    if(mask & IN_ISDIR)         event = "IN_ISDIR";
    if(mask & IN_UNMOUNT)       event = "IN_UNMOUNT";
}

//通过文件名找到 wd
int UCInotify::findWD(const std::string &file)
{
    map<int, string>::iterator it = m_watchFiles.begin();
    while(it != m_watchFiles.end())
    {
        string temp = it->second;
        if(temp == file)
        {
            return it->first;
        }
        it++;
    }
    return -1;
}

//重新监控文件
void UCInotify::Rewatch(const std::string &watch_name)
{
    vector<string> names;
    names.push_back(watch_name);
    AddWatchFile(names); //重新添加
    TRACE(6, "rewatch: " << watch_name);
}

/*监控目标被卸载
 *  该函数会检查所移除的文件是否存在，如果存在则从新添加监控
 * */
void UCInotify::eventUnmount(const std::string event_file, void *flags)
{
    if(flags == NULL) return ; //什么都不做

    UCInotify *pUI = (UCInotify*)flags;
    int ret = open(event_file.c_str(), O_EXCL, O_RDONLY);
    if(ret < 0)
    {
        if(errno == EEXIST)
        {
            pUI->Rewatch(event_file);
        }
        else
        {
            TRACE(1, "open err: " << strerror(errno));
        }
    }
    else
    {
        pUI->Rewatch(event_file);
    }
}