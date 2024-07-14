#!/bin/bash

readonly REPOS="entrypoints"
VERSION=$1
JSM=$2
FLAG=False
BRANCHLIST="2.6 2.9 2.10"

if [[ ${VERSION} == "" || ${JSM} == "" ]];then
    echo "args is empty, need 2 agrs, error" 
    exit -1 
fi 

function Check(){
    if [ ! -d  ~/workspace/${REPOS} ];then
        exit -1
    fi
    for i in ${BRANCHLIST}
    do
        if [[ $i == ${VERSION} ]];then
            FLAG=True
            break
        else 
            FLAG=False
        fi
    done
    if [[ ${FLAG} != True ]];then
        echo "entrypoints branch:" ${VERSION} "is error"
        exit
    fi
}

function StartEntrypoints(){
    Check 
    cd ~/workspace/${REPOS}/
    git pull && git checkout origin/V${VERSION} && git checkout -b QSD-${JSM} && code qpilot.repos
}

function AdjustFinish(){
    StartEntrypoints
    cd ~/workspace/${REPOS}/
    git add . && git commit -am "QSD-${JSM}" && \ 
    git diff $(git log --oneline | head -n 1) $(git log --oneline | head -n 1) 
    git push --set-upstream origin QSD-${JSM} &&  git checkout master && git pull 
}

function CleanUselessBranch(){
    AdjustFinish
    cd ~/workspace/${REPOS}/
    git checkout master && git branch -d QSD-${JSM}
}

function main(){
    CleanUselessBranch
}

main