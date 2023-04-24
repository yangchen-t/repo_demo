#!/bin/bash

function _param_tab() {
    case $COMP_CWORD in
    1)
        COMPREPLY=($(compgen -W "0.8 2.6 2.9 2.10" -- ${COMP_WORDS[COMP_CWORD]}))
        ;;
    2)
        if [[ ${COMP_WORDS[1]} == "0.8" ]]; then
            COMPREPLY=($(compgen -W "tj ck wh xm dl eh jk jj qp" -- ${COMP_WORDS[COMP_CWORD]}))
        fi
        if [[ ${COMP_WORDS[1]} == "2.6" ]]; then
            COMPREPLY=($(compgen -W "tj ck wh xm dl eh jk jj qp" -- ${COMP_WORDS[COMP_CWORD]}))
        fi
        if [[ ${COMP_WORDS[1]} == "2.9" ]]; then
            COMPREPLY=($(compgen -W "tj ck wh xm dl eh jk jj qp" -- ${COMP_WORDS[COMP_CWORD]}))
        fi
        if [[ ${COMP_WORDS[1]} == "2.10" ]]; then
            COMPREPLY=($(compgen -W "tj ck wh xm dl eh jk jj qp" -- ${COMP_WORDS[COMP_CWORD]}))
        fi
        ;;
    3)
        if [[ ${COMP_WORDS[2]} == "tj" ]]; then
            COMPREPLY=($(compgen -W "1 2" -- ${COMP_WORDS[COMP_CWORD]}))
        fi
        if [[ ${COMP_WORDS[2]} == "ck" ]]; then
            COMPREPLY=($(compgen -W "1" -- ${COMP_WORDS[COMP_CWORD]}))
        fi
        if [[ ${COMP_WORDS[2]} == "wh" ]]; then
            COMPREPLY=($(compgen -W "2" -- ${COMP_WORDS[COMP_CWORD]}))
        fi
        if [[ ${COMP_WORDS[2]} == "xm" ]]; then
            COMPREPLY=($(compgen -W "2" -- ${COMP_WORDS[COMP_CWORD]}))
        fi
        if [[ ${COMP_WORDS[2]} == "dl" ]]; then
            COMPREPLY=($(compgen -W "2" -- ${COMP_WORDS[COMP_CWORD]}))
        fi
        if [[ ${COMP_WORDS[2]} == "eh" ]]; then
            COMPREPLY=($(compgen -W "1" -- ${COMP_WORDS[COMP_CWORD]}))
        fi
        if [[ ${COMP_WORDS[2]} == "jk" ]]; then
            COMPREPLY=($(compgen -W "1 2" -- ${COMP_WORDS[COMP_CWORD]}))
        fi
        if [[ ${COMP_WORDS[2]} == "jj" ]]; then
            COMPREPLY=($(compgen -W "1 2" -- ${COMP_WORDS[COMP_CWORD]}))
        fi
        if [[ ${COMP_WORDS[2]} == "qp" ]]; then
            COMPREPLY=($(compgen -W "1 2" -- ${COMP_WORDS[COMP_CWORD]}))
        fi
        ;;
    4)
        if [[ ${COMP_WORDS[3]} == "1" ]]; then
            COMPREPLY=($(compgen -W "on off" -- ${COMP_WORDS[COMP_CWORD]}))
        fi
        if [[ ${COMP_WORDS[3]} == "2" ]]; then
            COMPREPLY=($(compgen -W "on off" -- ${COMP_WORDS[COMP_CWORD]}))
        fi
        ;;
    esac
}

complete -F _param_tab regression_adaptive.sh
