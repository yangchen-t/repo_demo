#! /bin/bash
systemfile1="/etc/os-release"
systemfile2="/usr/lib/os-release"
download_dir=
conf_file_path=/opt/apps/cn.huorong.esm/files/etc
downloader=
INST_CACHE_DIR='/tmp/.huorong_inst'

mktemp=`mktemp --version 2> /dev/null`
if [ "${mktemp#*"mktemp"}" != "$mktemp" ]; then
	download_dir=`mktemp  -d /tmp/.huorong_inst.XXXXXX`
else
	while :
	do
		suffix=`date +%s`
		download_dir=/tmp/.huorong_inst.$suffix
		if [ -d $download_dir ]; then
			sleep 1
			continue
		fi
		mkdir -p $download_dir
		break
	done
	
fi

curl=`curl --version 2> /dev/null`
wget=`wget --version 2> /dev/null`
if [ "${curl#*"curl"}" != "$curl" ]; then
	downloader="curl"
elif [ "${wget#*"Wget"}" != "$wget" ]; then
	downloader="wget"
else
	echo "Please instll curl or wget"
	exit 1
fi

framework=
if [ `uname -m` = "x86_64" ]; then
	framework="amd64"
elif [ `uname -m` = "aarch64" ]; then
	framework="aarch64"
elif [ `uname -m` = "mips64" ]; then
	framework="mips64le"
elif [ `uname -m` = "loongarch64" ]; then
	framework="loongarch64"
else
	echo "Unsupported CPU architecture: $(uname -m)."
	exit 1
fi

os=
handle_data() {
	line=$1
	if [ "${line#*\"}" != "$line" ]; then
		line=${line#*\"}
		line=${line%*\"}
	elif [ "${line#*\'}" != "$line" ]; then
		line=${line#*\'}
		line=${line%*\'}
	else
		line=${line#*'='}
	fi  
	line=`echo $line | tr 'A-Z' 'a-z'`
	if [ "${line#*' '}" != "${line}" ]; then
		t=${line#*' '}
		line=${line%*' '${t}}
	fi
}

read_os_release_id() {
	[ -r $1 ] && file=$1
	[ "$file" = "" ] && [ -r $2 ] && file=$2
	[ ! -n "$file" ] && return 1
	while read -r line
	do
		[ "${line#*"ID="}" = "$line" ] && continue
		[ "${line#*"_ID"}" != "$line" ] && continue
		handle_data $line
		os="00_linux_client_v2_${framework}_desktop_${line}"
		break
	done < $1
	return 0
}

read_os_release_version() {
	[ -r $1 ] && file=$1
	[ "$file" = "" ] && [ -r $2 ] && file=$2
	[ ! -n "$file" ] && return 1
	while read -r line
	do
		[ "${line#*"VERSION="}" = "$line" ] && continue  
		handle_data $line
		[ "$os" = "" ] && break
		os=${os}_${line}
		break
	done < $file
	return 0
}

read_os_release_id $systemfile1 $systemfile2
read_os_release_version $systemfile1 $systemfile2
[ "$os" = "" ] && os="00_linux_client_v2_${framework}_desktop_linux"

instfn=
host=$HRADDR
parse_host() {
	if [ ! -n "$instfn" ]; then
		return
	fi

	host=${instfn#*(}
	if [ "$host" = "$instfn" ]; then
		host=
		return
	fi
	bracket=')'
	while :
	do
		if [ "${host#*$bracket}" != "$host" ]; then
			host=${host%)*}
		else
			break
		fi
	done
	if [ "${host#*"http_"}" != "$host" ]; then
		t="http://"
		host=${host#*"http_"}
		host=${t}"${host}"
	fi
	if [ "${host#*"https_"}" != "$host" ]; then
		t="https://"
		host=${host#*"https_"}
		host=${t}"${host}"
	fi
	while :
	do
		if [ "${host%_*}" != "$host" ]; then
			t=":"${host##*_}
			host=${host%_*}
			host=${host}"$t"
		else
			break
		fi
	done
}

if [ ! -n "$host" ]; then
	instfn="${0##*/}"
	parse_host
fi

jRespone=
check_update_link() {
	if [ "${host%/*}" != "http:/" ] && [ "${host%/*}" != "https:/" ]; then
			host=${host%?}
	fi

	if [ "${host%_*}" != "$host" ]; then
		t=":"${host##*_}
		host=${host%_*}
		host=${host}"$t"
	fi
	
	http_code=0
	if [ "$downloader" = "curl" ]; then
		http_code=`curl -k -s -o /dev/null -w "%{http_code}" $host/upgrade/upgrade2?product=$os `
		if [ ! $http_code -eq 200 ]; then
			echo -e "\033[31mError \033[0m" response code: $http_code
			host=
		fi
	else
		jRespone=`wget -q --output-document=- $host/upgrade/upgrade2?product=$os --no-check-certificate`
		if [ "$jRespone" != "" ]; then
			http_code=200	
		else
			echo -e "\033[31mError \033[0m" wget response is null
		fi
	fi

	return $http_code
}

while :
do
	if [ ! -n "$host" ]; then
		read -p "please input huorong center domain[:port]" host
	fi

	if [ ! -n "$host" ]; then
		continue
	fi
	
	if [ "${host#*"https://"}" = "$host" ]; then
		if [ "${host#*"http://"}" = "$host" ]; then
			t="https://"
			host=${t}$host
		fi
	fi
		
	check_update_link
	if [ $? -eq 200 ]; then
		break
	else 
		host=
	fi
done

handle_download_addr() {
	if [ "$downloader" = "curl" ]; then
		jRespone=`curl -s -k $host/upgrade/upgrade2?product=$os -H "Accept: application/json"`
	fi

	jResult=
	jData=${jRespone##*'{'}
	while :
	do
		jResult=${jData%%','*}
		if [ "${jResult#*"relative"}" != "$jResult" ]; then
			jResult=${jResult#*':'}
			jResult=${jResult#*'"'}
			jResult=${jResult%'"'*}
			break
		fi
		jData=${jData#*','}
	done
	
	if [ "$downloader" = "curl" ]; then
		curl -k -s -L $host/${jResult}inst/update.deb -o $download_dir/update.deb >/dev/null 2>&1
	else
		wget -P $download_dir $host/${jResult}inst/update.deb >/dev/null --no-check-certificate 2>&1
	fi
}

handle_download_addr
if [ "${os#*"uos"}" != "$os" ]; then
	[ -d $INST_CACHE_DIR ] && rm -rf $INST_CACHE_DIR
	mkdir -p $INST_CACHE_DIR
	echo $host > $INST_CACHE_DIR/update_link.txt
	mv $download_dir/update.deb $INST_CACHE_DIR/update.deb
	deepin-deb-installer $INST_CACHE_DIR/update.deb
	rm -rf $INST_CACHE_DIR
else
	sudo UPDATE_LINK=$host UPDATE_FILE=$download_dir/update.deb dpkg -i $download_dir/update.deb
fi

rm -rf $download_dir