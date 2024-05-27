#!/bin/bash

# set -e  # ReturnZeroExit
set -x  # DebugMode
set -u  # NullVarCheck

exec 11> >( socat -t 0 stdin fd:1 )
exec 12> >( socat -t 0 stdin fd:1 ) #do not use stderr
exec 101> >( sed -u 's/\r/\r\t\t\t\t\t\t\t/g' | logger -p local0.info -t $0 )      # info：一般信息或事件的记录。
exec 102> >( sed -u 's/\r/\r\t\t\t\t\t\t\t/g' | logger -p local0.notice -t $0 )    # notice：重要事件的普通通知。
exec 103> >( sed -u 's/\r/\r\t\t\t\t\t\t\t/g' | logger -p local0.warning -t $0 )   # warning：警告消息，表明发生了异常情况。
exec 104> >( sed -u 's/\r/\r\t\t\t\t\t\t\t/g' | logger -p local0.err -t $0 )       # err：错误消息，但不会影响系统运行。
exec 105> >( sed -u 's/\r/\r\t\t\t\t\t\t\t/g' | logger -p local0.crit -t $0 )      # crit：临界状态，指示发生了严重错误。
exec 106> >( sed -u 's/\r/\r\t\t\t\t\t\t\t/g' | logger -p local0.alert -t $0 )     # alert：需要立即采取行动的警报。
exec 107> >( sed -u 's/\r/\r\t\t\t\t\t\t\t/g' | logger -p local0.emerg -t $0 )     # emerg：紧急情况，表示系统不可用。

exitcode()
{
    local _code=$1
    exec >&11-
    exec >&12-
    exec >&101-
    exec >&102-
    exec >&103-
    exec >&104-
    exec >&105-
    exec >&106-
    exec >&107-
    sleep 0.02
    exit ${_code}
}

test()
{
    echo "1231231" >&101

}

test && exitcode 0