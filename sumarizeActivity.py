#!/usr/bin/python
import os
import re
import csv
 
saida = open("timelineUsersPinterest.txt","w")
for arq in os.listdir("./profiles"):
	try:
		for board in os.listdir("./profiles/"+arq+"/boards/"):
			
			try:
				File= open("./profiles/"+arq+"/boards/"+board+ "/attributes", "r")
				csvFile = csv.reader(File,delimiter=';')
				csvFile.next()
				for row in csvFile:
					category = row[1]
				photos = open('./profiles/'+arq+'/boards/'+board+'/timeline',"r")
				csvPhotos = csv.reader(photos,delimiter=";")
				for photo in csvPhotos:
					saida.write(arq+";"+category+";"+photo[0]+";"+photo[1]+"\n")
			except :
				print "usuario ("+ arq+") nao tem o seguinte board attribute: "+board
	except :
		print "usuario ("+ arq+"): nao existe mais"

