#!/usr/bin/python
import os
import re
for arq in os.listdir("./profiles"):
	qtd = 0
	try:
		for board in os.listdir("./profiles/"+arq+"/boards/"):
			nPhotos = [f for f in os.listdir('./profiles/'+arq+'/boards/'+board) if re.match(r'[0-9]+', f)]
			qtd += len(nPhotos)
	except :
		print "usuario ("+ arq+") nao existe mais"
	print arq +","+str(qtd)	
