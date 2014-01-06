#!/usr/bin/python
import os
import re
import csv
import logging
import gzip
import re
 
#loggin setup
logging.basicConfig(filename="repinDesc.log", filemode="a", level=logging.INFO, format="[ %(asctime)s ] %(levelname)s : %(message)s")

saida = open("repinDesc.txt","w")

#build header
saida.write("pinId;nLikes;nRepins;isRepin;desc\n")
for arq in os.listdir("./profiles"):
	try:
			
      		logging.info("["+arq+"]:  iniciando" )
		for board in os.listdir("./profiles/"+arq+"/boards/"):
			
			try:
				photos = open('./profiles/'+arq+'/boards/'+board+'/timeline',"r")
				csvPhotos = csv.reader(photos,delimiter=";")
				for photo in csvPhotos:
					
					pinPage = gzip.open('./profiles/'+arq+'/boards/'+board+'/'+photo[0],"r").read()
					desc = re.findall('<meta property="og:description" name="og:description" content="(.*)" data-app="">', pinPage)[0].strip()
					repin = re.findall('<h3 class="title">Repinned from</h3>',pinPage)
					likes = re.findall('<meta property="pinterestapp:likes" name="pinterestapp:likes" content="(.*)" data-app="">',pinPage)[0].strip()
					repins = re.findall('<meta property="pinterestapp:repins" name="pinterestapp:repins" content="(.*)" data-app="">',pinPage)[0].strip()
					
					if repin:
						repin = 1
					else:
						repin = 0		
					saida.write(photo[0]+";"+str(likes)+";"+str(repins)+";" + str(repin) +";"+ desc+"\n")
			except :
      				logging.error("["+ arq+"]: nao tem o seguinte board attribute: "+board)
	except :
      		logging.error("["+ arq+"]: nao existe mais")

