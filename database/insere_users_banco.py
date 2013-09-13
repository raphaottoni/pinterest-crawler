import MySQLdb 

db = MySQLdb.connect("localhost","root","Ow,CEh24","pinterestTwitter")
cursor = db.cursor()


for arquivo in open("silberman_users.txt","r"):
  cursor.execute("insert into usersToCollect (pinterestID) values ('"+arquivo.strip()+"')")
  db.commit()
