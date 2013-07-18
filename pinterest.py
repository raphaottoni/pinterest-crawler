import urllib2
import time
import random
import socket
import MySQLdb
from config import *
import os

class Pinterest:
  #------inicializacao -------#
  def __init__(self, verbose=0):
    self.db = MySQLdb.connect(host,user,password,database)
    self.cursor = self.db.cursor()
    self. cursor.connection.autocommit(True)


  def fetch(self,url):
    done=0
    while(not done):
      try:

        # Nao funciona mais pq virou tudo javascript!!!!! #

        #req = urllib2.Request(url, headers={'User-Agent' : "M"}) #,"Accept-Encoding": "gzip"})
        #con = urllib2.urlopen( req )
        #html = con.read()
        #con.close()

        html = os.popen("phantomjs ./tst.js "+url).read()

        done=1;
      except urllib2.HTTPError, e:
        #log = open("/var/tmp/rapha/log","a+")
        #log.write(str(e.msg) +"'"+ url+ "' \n")
        print (str(e.msg) +"'"+ url+ "' \n")
        #log.close()
        time.sleep(random.randint(1,5))
        if ( hasattr(e, 'code') and e.code == 404):
          return 1
        continue
      except urllib2.URLError, e:
        #log = open("/var/tmp/rapha/log","a+")
        #log.write(str(e.reason[1])+ "'"+ url +"' \n")
        print (str(e.reason[1])+ "'"+ url +"' \n")
        #log.close()
        time.sleep(random.randint(1,5))
        if ( hasattr(e, 'code') and e.code == 404):
          return 1
        continue
      except socket.timeout:
        #log = open("/var/tmp/rapha/log","a+")
        #log.write("Time out pelo sockect - '"+ url + "' \n")
        print ("Time out pelo sockect - '"+ url + "' \n")
        #log.close()
        time.sleep(random.randint(1,5))
        continue
      except socket.error, e:
        #log = open("/var/tmp/log","a+")
        #log.write("sockect - '"+ str(e) + "' \n")
        print ("sockect - '"+ str(e) + "' \n")
        #log.close()
        time.sleep(random.randint(5,15))
        continue
      except Exception , e :
        #log = open("/var/tmp/log","a+")
        #log.write("sockect - '"+ str(e) + "' \n")
        print ("sockect - '"+ str(e) + "' \n")
        #log.close()
        time.sleep(random.randint(2,6))
        continue
    return html

  def snowBall(self):
          self.cursor.execute("select pinterestID from fatos where statusIDs is null or statusIDs = 0 limit 1")
          self.db.commit()
          return self.cursor.fetchone()[0]
  def getIDtoCrawl(self):
          self.cursor.execute("select pinterestID from usersToCollect where statusColeta is null or statusColeta = 0 limit 1")
          self.db.commit()
          #return self.cursor.fetchone()[0]
          return "raphaottoni"


  def insereID(self,pinterestID):
        try:
          self.cursor.execute("insert into fatos (pinterestID) values ('"+pinterestID+"')")
          self.db.commit()
        except MySQLdb.IntegrityError, e:
          log = open("/var/tmp/log","a+")
          log.write("Erro de integridade do banco: '"+ str(e)+ "' \n")
          log.close()
  def statusColetaIDs(self,pinterestID,valor):
        try:
          self.cursor.execute("update usersToCollect set statusIDs ='"+valor+"' where pinterestID = '"+pinterestID+"'")
          self.db.commit()
          print "update usersToCollect set statusIDs ='"+valor+"' where pinterestID = '"+pinterestID+"'"
        except Exception, e:
          log = open("/var/tmp/log","a+")
          log.write("Erro de integridade do banco: '"+ str(e)+ "' \n")
          log.close()
  def statusColeta(self,pinterestID,valor, dominio):
        try:
          self.cursor.execute("update usersToCollect set statusColeta ='"+valor+"' , crawler = '"+dominio+"' where pinterestID = '"+pinterestID+"'")
          self.db.commit()
          print "update usersToCollect set statusColeta ='"+valor+"' , crawler = '"+dominio+"' where pinterestID = '"+pinterestID+"'"
        except Exception, e:
          log = open("/var/tmp/log","a+")
          log.write("Erro de integridade do banco: '"+ str(e)+ "' \n")
          log.close()
  def nPinsUser(self,pinterestID,valor):
        try:
          self.cursor.execute("insert into deltaPinUsers (pinterestID,nPins) values  ('"+pinterestID+"' , '"+valor+"')")
          self.db.commit()
          #print ("insert into deltaPinUsers (pinterestID,nPins) values  ('"+pinterestID+"' , '"+valor+"')")
        except Exception, e:
          print str(e)
          log = open("/var/tmp/log","a+")
          log.write("Erro de integridade do banco: '"+ str(e)+ "' \n")
          log.close()

