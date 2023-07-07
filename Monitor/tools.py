import subprocess


def cpuExec(process):
    return subprocess.getoutput("cpustat 0.333 1 -l -n 10 -x | grep {0} | awk {1} ".format(process, "'{print$1}'"))
def memExec(process):
    return subprocess.getoutput("pidstat -r 1 1  | grep {0} | head -n 1 | awk {1} ".format(process, "'{print$7}'")), \
        subprocess.getoutput("pidstat -r 1 1  | grep {0} | head -n 1 | awk {1} ".format(process, "'{print$8}'")) 