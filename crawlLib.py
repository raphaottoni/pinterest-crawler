import pinterest
import sys,fcntl,csv,urllib2
import time,random
import os.path
import gzip
from datetime import datetime
from bs4 import BeautifulSoup
from django.utils.encoding import smart_str, smart_unicode
import re

class Crawler:

  #------inicializacao -------#
  def __init__(self, verbose=0):
    self.pinterest = pinterest.Pinterest()
    self.host = "localhost"

  #------------------------------------#
  #--funcao de coleta dadps  completa--#
  #------------------------------------#
  #-AINDA NAO TA PRONTO ---------------#
  #------------------------------------#
  def gatherInfo(self,pinterestID):
    print "iniciei parse de " +pinterestID
    path="profiles/"+pinterestID
    if not os.path.exists(path): os.makedirs(path)
    profile = gzip.open(path+"/profile","w")
    html = self.pinterest.fetch("http://pinterest.com/"+ pinterestID + "/?d")

    if ( html == 1):
      return 1

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
    atributos.write(header+smart_str(att))
    atributos.close()

    print "Coletando Boards"
    #Salva os boards ----- Primeira pagina so vem os 49! nao 50!!!! OMG
    pathBoards="profiles/"+pinterestID+"/boards"
    if not os.path.exists(pathBoards): os.makedirs(pathBoards)


    boards = re.findall('<a href="(.*)" class="boardLinkWrapper">',html)
    saida = open("raphaottoni","w")
    saida.write(html)
    saida.close()

    for board in boards:
        print board
        albumLink = board
        owner = albumLink.split("/")[1]
        albumName = albumLink.split("/")[2]
        if not os.path.exists(pathBoards+"/"+albumName): os.makedirs(pathBoards+"/"+albumName)
        print "http://pinterest.com"+ albumLink
        htmlBoard = self.pinterest.fetch("http://pinterest.com"+ albumLink)
        category= re.search('name="pinterestapp:category" content="(.*)" ',htmlBoard).group(1).strip()
        saida= open("raphaottoni","w")
        saida.write(htmlBoard)
        saida.close()
        followers = re.search('name="followers" content="(.*)" ',htmlBoard).group(1).strip()
        title = re.search('name="og:title" content="(.*)" ',htmlBoard).group(1).strip()
        nPins= re.search('name="pinterestapp:pins" content="(.*)" ',htmlBoard).group(1).strip()

        board = gzip.open(pathBoards+"/"+albumName+"/initialPage","w")
        board.write(htmlBoard)
        board.close()
        #escreve atributos
        atributos = open(pathBoards+"/"+albumName+"/attributes","w")
        header="albumLink;owner;albumName;title;nFollowers;nPins;date\n"
        att=""+albumLink+";"+owner+";"+albumName+";"+title+";"+followers+";"+nPins+";"+str(datetime.now())
        atributos.write(header+smart_str(att))
        atributos.close()





    #    #talvez tirar esse if, pq nao precisa ser dono do album
    #    if (albumLink.split("/")[1] == pinterestID):
    #      qtdPaginas = int(nPins)/50
    #      j = 0
    #      parada = 0
    #      for i in range(qtdPaginas+1):

    #        if (parada == 1):
    #          break
    #        htmlBoard = self.pinterest.fetch("http://pinterest.com/"+albumLink +"?page="+str(i+1))
    #        #aki entra a parte de olhar os pins
    #        paginaBoard= BeautifulSoup(htmlBoard)

    #        for pin in paginaBoard.find(id="ColumnContainer").find_all("a"):
    #          if ( parada == 1):
    #            board = open(pathBoards+"/"+albumName+"/attributes","w")
    #            board.write("newPins,nPins;category;followers;owner;albumName\n"+str(j)+";"+nPins+";"+category+";"+followers+";"+dono+";"+albumName)
    #            board.close()
    #            break
    #          if(pin.get("class")):
    #            if pin.get("class")[0] == "PinImage":
    #              #print pin.get('href')
    #              htmlPin= self.pinterest.fetch("http://pinterest.com"+pin.get('href'))

    #              # Fucking workout - Pinterest Html came with tag 'class' glue together with previous tag - beautifulSoup cant handle that!!!
    #              htmlPin = htmlPin.replace('2F"class="Button RedButton Button18','2F" class="Button RedButton Button18')
    #              paginaPin = BeautifulSoup(htmlPin)
    #              timeAgo = paginaPin.find(id="PinnerStats").contents[0].strip()

    #              if (timeAgo.find("week") ==  -1 and timeAgo.find("year") == -1 and timeAgo.find("month") == -1):
    #                #print paginaPin.find(id="PinnerStats").contents[0].strip()
    #                saida= gzip.open(pathBoards+"/"+albumName+"/"+str(j+1),"w")
    #                saida.write(htmlPin)
    #                saida.close()
    #                j +=1
    #              else:
    #                parada = 1


            #board = gzip.open(pathBoards+"/"+albumName+"/"+str((i+1)),"w")
            #board.write(htmlBoard)
            #board.close()

    return 0
