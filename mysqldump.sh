#!/bin/sh
datetime=`date +%Y%m%d_%H%M%S`
#db=wenxiaomao
db2=firekylin
#mysqldump $table -uroot -pHello@123 > /root/wen/mysqldump/$db$datetime.sql
mysqldump firekylin -uroot -pHello@123 > /root/wen/mysqldump/$db2$datetime.sql
