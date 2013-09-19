#! /bin/bash

# $1 = name of the hd partion
# $2 = number of clients
# $3 = log file

echo "Reset at $(date):  $(echo $( mysql -u root -pOw,CEh24 pinterestTwitter -e "select count(*) from usersToCollect where statusColeta=2;") | cut -d" " -f2 ) users fully collected" >> $3
#Mata o que 
killall client.py
killall server.py
killall phantom.js
mysql -u root -pOw,CEh24 pinterestTwitter < /data/$1/pinterest-crawler/daily_reset/reset.sql
sleep 2
cd /data/$1/pinterest-crawler/
nohup /data/$1/pinterest-crawler/server.py &
sleep 2
for i in $( seq $2 )
do
   nohup /data/$1/pinterest-crawler/client.py localhost &
done 

