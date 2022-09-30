#!/bin/bash

echo "欢迎你的使用Reptile！该脚本进程如下↓使用该脚本安装所有的依赖后，下次使用直接命令 python xx.py 或 python reptile/xx.py"
echo ""
echo ""
echo "换国内源→更新源→下载git→下载python→下载python2→下载python3→安装Beautifulsoup4库→安装requests库→安装datetime库→下载Reptile→进入Reptile文件夹→手动进入Reptile"
read -r -p "按回车键开始下载！" input
	if [ -d /data/data/com.termux/files/usr/etc/termux/mirrors/china ]; then
	rm -rf /data/data/com.termux/files/usr/etc/termux/chosen_mirrors
	ln -s /data/data/com.termux/files/usr/etc/termux/mirrors/china /data/data/com.termux/files/usr/etc/termux/chosen_mirrors
	fi
	sed -i 's@^\(deb.*stable main\)$@#\1\ndeb https://mirrors.bfsu.edu.cn/termux/termux-packages-24 stable main@' $PREFIX/etc/apt/sources.list && yes | pkg update 
	sed -i 's@^\(deb.*stable main\)$@#\1\ndeb https://mirrors.bfsu.edu.cn/termux/termux-packages-24 stable main@' $PREFIX/etc/apt/sources.list && pkg update
read -r -p "完成换源！按回车键继续" input
echo `cd`
echo `pkg install git`
read -r -p "git下载完成！按回车键继续" input
echo `pkg install python`
read -r -p "python下载完成！按回车键继续" input
echo `pkg install python2`
read -r -p "python2下载完成！按回车键继续" input
echo `pkg install python3`
read -r -p "python3下载完成！按回车键继续" input
echo `pip install Beautifulsoup4`
read -r -p "Beautifulsoup4下载完成！按回车键继续" input
echo `pip install requests`
read -r -p "requests下载完成！按回车键继续" input
echo `pip install datetime`
read -r -p "datetime下载完成！按回车键继续" input
echo `git clone https://gitee.com/sansjtw/reptile`
read -r -p "Reptile下载完成按回车键继续" input
echo `cd reptile`
read -r -p "已进入Reptile文件夹！按回车键继续" input
echo ""
echo ""
echo "安装依赖和下载完成！请自行手动输入命令 cd&&cd reptile&&python xx.py 之后你也可以不用运行该脚本，因为该脚本只是用于安装依赖，并非直接运行Reptile！"
echo ""
read -r -p "按回车键返回" input
exit

                                  