#!/bin/bash 

# NOTE regression test
function RegressionTesting()
{
    declare -A SupervisorConfig
    SupervisorConfig=(
        [cntjic]="tj_" \
        [cntjitpy]="cntjitpy_" \
        [cntjija]="cntjija" \
        [cnxmehr]="xm_" \
        [cnxmeyh]="cnxmeyh_" \
        [cnjxizp]="cnjxizp_" \
        [cnelh]="eh_" \
        [cndlidct]="dl_" \
        [cnwha]="wh_" \
        [cnalsck]="ceke_" \
        [cntshjtg]="cntshjtg_" \
        [cnwxijk]="Q_jk_" \
        [cntzhjj]="T_cntzhjj_" \
        [cnshaqp]="Q_qp_" \
        [cnshalj]="cnshalj_" \
        [cncqisls]="Q_cncqisls_" \
        [cnbtomdl]="cnbtomdl_" \
        [mxvlkica]="Q_ica_" \
        [sesdgctn]="W_ctn_" \
        [dkahs]="W_ctn_" \
        [cnrzh]="cnrzh_" \
        [sgpsa]="sgpsa_" 
    )
    readonly SingleDcuProject=("cntjic" "cnalsck" "cnbtomdl" "cnelh")
    readonly FileName=/opt/qomolo/utils/qpilot_setup/2.10/.project_name
    readonly Dcu=/opt/qomolo/utils/devops_test_agent/.env
    readonly _tmp="2.10.conf"
    readonly DcuType_105="105_"
    readonly DcuType_106="106_"
    _S="supervisor_"

    if [ -f  ${FileName} ];then
        if [ ${FileName} ]; then
            local tmp=$(cat ${FileName})
            for p in "${SingleDcuProject[@]}";do
                if [[ ${tmp} == ${p} ]];then
                    SUPER=${SupervisorConfig[${p}]}${_S}${_tmp}
                    return
                fi 
            done
            if [ -f ${Dcu} ];then
                case $(cat ${Dcu}) in 
                1)
                    SUPER=${SupervisorConfig[${tmp}]}${_S}${DcuType_105}${_tmp} ;;
                2)
                    SUPER=${SupervisorConfig[${tmp}]}${_S}${DcuType_106}${_tmp} ;;
                *)
                    echo "Dcu Type error" ;;
                esac
            else 
                echo "${Dcu} is not exist"
            fi
        fi
    fi
}
function main()
{
    RegressionTesting
    ENVFILE="/opt/qomolo/utils/qpilot_setup/2.10/.env"
    if [ -f ${ENVFILE} ];then
        echo nvidia | sudo -S chown -R nvidia.nvidia ${ENVFILE}
	    echo nvidia | sudo -S sed -i 's/\(SUPER=\).*/\1'${SUPER}'/' ${ENVFILE}
    fi 
}
main
