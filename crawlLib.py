import pinterest
import sys,fcntl,csv,urllib2
import time,random
import os.path
import gzip
from datetime import datetime
import re
from datetime import *

class Crawler:

  #------inicializacao -------#
  def __init__(self, verbose=0):
    self.pinterest = pinterest.Pinterest()
    self.host = "localhost"

  def findTime(self,timeAgo):
    now = datetime.now()
    time = -1
    if(timeAgo.find("now") != -1):
        time = now
    else:
        tempo = [int(s) for s in timeAgo.split() if s.isdigit()][0]
        if(timeAgo.find("sec") != -1):
            time = now - timedelta(seconds=tempo)
        elif (timeAgo.find("minut") != -1):
            time = now - timedelta(minutes=tempo)
        elif(timeAgo.find("hour") != -1):
            time = now - timedelta(hours=tempo)
    return time


  def gatherInfo(self,pinterestID):
    print "iniciei parse de " +pinterestID
    path="profiles/"+pinterestID
    if not os.path.exists(path): os.makedirs(path)
    profile = gzip.open(path+"/profile","w")
    html = self.pinterest.fetch("http://pinterest.com/"+ pinterestID + "/?d")

    print "voltou a resposta"
    if (html == 1):
        print "voltando pq deu erro - usuario nao existe"
        return

    profile.write(html)
    profile.close()

    print "Coletando attributes"
    nPins = re.search('name="pinterestapp:pins" content="(.*)" ',html).group(1).strip()
    nBoards = re.search('name="pinterestapp:boards" content="(.*)" ',html).group(1).strip()
    nFollowing= re.search('name="pinterestapp:following" content="(.*)" ',html).group(1).strip()
    nFollower= re.search('name="pinterestapp:followers" content="(.*)" ',html).group(1).strip()



    #escreve atributos
    atributos = open(path+"/attributes","w")
    header="nBoards;nPins;nFollower;nFollowing\n"
    att=""+nBoards+";"+nPins+";"+nFollower+";"+nFollowing
    atributos.write(header+att)
    atributos.close()

    print "Coletando Boards"
    #Salva os boards ----- Primeira pagina so vem os 49! nao 50!!!! OMG
    pathBoards="profiles/"+pinterestID+"/boards"
    if not os.path.exists(pathBoards): os.makedirs(pathBoards)


    boards = re.findall('<a href="(.*)" class="boardLinkWrapper">',html)

    for board in boards:
        print board
        albumLink = board
        owner = albumLink.split("/")[1]
        albumName = albumLink.split("/")[2]
        if not os.path.exists(pathBoards+"/"+albumName): os.makedirs(pathBoards+"/"+albumName)
        print "http://pinterest.com"+ albumLink


        #cralw the first pin page of the boad (25 items at most)
        htmlBoard = self.pinterest.fetchPins("http://pinterest.com"+ albumLink, "0")
        nPinsOnBoard = re.search('name="pinterestapp:pins" content="(.*)" ',htmlBoard).group(1).strip()
        title = re.search('name="og:title" content="(.*)" ',htmlBoard).group(1).strip()
        nFollowersBoard= re.search('name="followers" content="(.*)" ',htmlBoard).group(1).strip()
        category= re.search('name="pinterestapp:category" content="(.*)" ',htmlBoard).group(1).strip()
        pinsRead = set ()
        coleta =1
        info = open(pathBoards+"/"+albumName+"/timeline","a")
        print nPinsOnBoard


        #write metainfo of the board
        saida = open(pathBoards+"/"+albumName+"/attributes","w")
        header="title;category;nPins;nFollower;boardLink\n"
        att=""+title+";"+ category+ ";"+nPinsOnBoard+";"+nFollowersBoard+";"+albumLink
        saida.write(header+att)
        saida.close()

        #write the first page of the board
        saida = gzip.open(pathBoards+"/"+albumName+"/firstPage","w")
        saida.write(htmlBoard)
        saida.close()


        #crawl until find some content not generated today
        while(coleta):
            pins = re.findall('<a href="(.*)" class="pinImageWrapper "',htmlBoard)
            for pin in pins:

               if not (pin in pinsRead):
                  htmlPin  = self.pinterest.fetchSimple("http://pinterest.com"+ pin)
                  timeAgo = re.search('class="commentDescriptionTimeAgo">(.*)</span>',htmlPin)
                  timeCreate= self.findTime(timeAgo.group(1))
                  if ( timeCreate  == -1):
                      coleta = 0
                      break
                  pinsRead.add(pin)
                  print len(pinsRead)

                  #save the pin-html
                  pinStream = gzip.open(pathBoards+"/"+albumName+"/"+pin.split("/")[2],"w")
                  pinStream.write(htmlPin)
                  pinStream.close()
                  #add the meta info telling when the content was created
                  info.write(pin.split("/")[2] +";" + str(timeCreate) + ";" + str(datetime.now())+"\n")




            if (coleta != 0 ):
                if int(nPinsOnBoard) > len(pinsRead):
                   remaning = int(nPinsOnBoard) - len(pinsRead)
                   if (remaning >= 25 ):
                       nRequest = len(pinsRead) + 25
                   else:
                       nRequest = len(pinsRead) + remaning
                   #print "Pedindo mais " + str(nRequest)
                   htmlBoard = self.pinterest.fetchPins("http://pinterest.com"+ albumLink, str(nRequest) )
                else:
                    break

        info.close()





    #    #talvez tirar esse if, pq nao precisa ser dono do album
    #    if (albumLink.split("/")[1] == pinterestID):
    #      qtdPaginas = int(nPins)/50
    #      j = 0
    #      parada = 0
    return 0
