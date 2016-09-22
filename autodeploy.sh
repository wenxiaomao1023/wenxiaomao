#!/bin/sh

cd /root/wen/wenxiaomao
git fetch
git stash
git rebase
git stash pop

pn=`ps -eo pid,comm | grep uwsgi | awk 'END{print NR}'`
echo $pn
if [ $pn -ne 0 ];then
	pid=`ps -eo pid,comm | grep uwsgi | awk 'NR==1{print $1}'`
	kill -9 $pid
	echo "Kill pid $pid DONE"
else
	echo "No uwsgi process"
fi
sleep 5 
/usr/bin/uwsgi --ini /root/wen/wenxiaomao/wen_uwsgi.ini
