#! /bin/bash

#Mata o que 
killall client.py
killall server.py
killall phantom.js
mysql -u root -pOw,CEh24 pinteresTwitter < /data/haddock/pinterest-crawler/daily_reset/reset.sql
nohup /data/haddock/pinterest-crawler/server.py &

for i in $( seq 20 )
do
   nohup /data/haddock/pinterest-crawler/client.py localhost &
done 

echo "Reset at $(date):  $(echo $( mysql -u root -pOw,CEh24 pinterestTwitter -e "select count(*) from usersToCollect where statusColeta=2;") | cut -d" " -f2 ) users fully collected" >> $1

