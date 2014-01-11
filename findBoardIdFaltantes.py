#!/usr/bin/python
import os
import re
import csv
import logging
import gzip
import re
 
#loggin setup
logging.basicConfig(filename="findBoardID.log", filemode="a", level=logging.INFO, format="[ %(asctime)s ] %(levelname)s : %(message)s")

saida = open("findBoardIdFaltantes.txt","w")


#lista dos faltantes 
faltantes = set()

for faltante in open("pinsFaltantesBoardId.data","r"):
	faltantes.add(faltante.strip())


#build header
saida.write("pinId;boardId\n")
for arq in os.listdir("./profiles"):
	try:
			
      		logging.info("["+arq+"]:  iniciando" )
		for board in os.listdir("./profiles/"+arq+"/boards/"):
			
			try:
				photos = open('./profiles/'+arq+'/boards/'+board+'/timeline',"r")
				csvPhotos = csv.reader(photos,delimiter=";")
				for photo in csvPhotos:
					
					if photo[0]  in faltantes:
						pinPage = gzip.open('./profiles/'+arq+'/boards/'+board+'/'+photo[0],"r").read()
						boardId = re.findall('<meta property="pinterestapp:pinboard" name="pinterestapp:pinboard" content="(.*)" data-app="">',pinPage)[0].strip()
						
						saida.write(photo[0]+";"+str(boardId.replace("http://www.pinterest.com/",""))+"\n") 
			except :
      				logging.error("["+ arq+"]: nao tem o seguinte board attribute: "+board)
	except :
      		logging.error("["+ arq+"]: nao existe mais")

