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
    #comeca o parse
    soup = BeautifulSoup(html)


    metas = soup.findAll("meta")
    for meta in metas:
      if meta.get("property") == "pinterestapp:pins":
        #print "pins "+ meta.get("content")
        nPins = meta.get("content").replace(",","")
      elif meta.get("property") == "pinterestapp:boards":
        #print "boars" + meta.get("content")
        nBoards = meta.get("content").replace(",","")
      elif meta.get("property") == "pinterestapp:following":
        #print "following" + meta.get("content")
        nFollowing= meta.get("content").replace(",","")
      elif meta.get("property") == "pinterestapp:followers":
        #print "followers" + meta.get("content")
        nFollower= meta.get("content").replace(",","")
      elif meta.get("property") == "pinterestapp:followers":
        #print "followers" + meta.get("content")
        nFollower= meta.get("content").replace(",","")



    ##escreve atributos
    #atributos = open(path+"/attributes","w")
    #header="nBoards;nPins;nFollower;nFollowing\n"
    #att=""+nBoards+";"+nPins+";"+nFollower+";"+nFollowing
    #atributos.write(header+smart_str(att))
    #atributos.close()

    print "Coletando Boards"
    #Salva os boards ----- Primeira pagina so vem os 49! nao 50!!!! OMG
    pathBoards="profiles/"+pinterestID+"/boards"
    if not os.path.exists(pathBoards): os.makedirs(pathBoards)


    boards = re.findall('<a href="(.*)" class="boardLinkWrapper">',html)
    saida = open("raphaottoni","w")
    saida.write(html)
    saida.close()
    print re.findall('href="(.*)"',html)

    for board in boards:
        print board

    #for link in soup.find(id="ColumnContainer").findAll("h3"):
    #  if link.findAll("a"):
    #    albumLink = link.findAll("a")[0].get("href")
    #    dono = albumLink.split("/")[1]
    #    albumName = link.findAll("a")[0].get("href").split("/")[2]
    #    if not os.path.exists(pathBoards+"/"+albumName): os.makedirs(pathBoards+"/"+albumName)
    #    #print  "url do album" + albumLink
    #    htmlBoard = self.pinterest.fetch("http://pinterest.com/"+ albumLink)
    #    soup2= BeautifulSoup(htmlBoard)
    #    for meta in  soup2.find("head").findAll("meta"):
    #      if (meta.get("property") == "pinterestapp:category"):
    #        category= meta.get("content")
    #      elif (meta.get("property") == "pinterestapp:followers"):
    #        followers= meta.get("content").replace(",","")
    #    board = gzip.open(pathBoards+"/"+albumName+"/paginaInicial","w")
    #    board.write(htmlBoard)
    #    board.close()
    #    soupBoard = BeautifulSoup(htmlBoard)
    #    nPins = soupBoard.find(id="BoardStats").findAll("strong")[-1].text.replace(",","")

    #    #Marca o timestap de comeco da coleta do album
    #    Date = datetime.now()
    #    tempo= open(pathBoards+"/"+albumName+"/datetime","w")
    #    tempo.write(str(Date))
    #    tempo.close()

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
