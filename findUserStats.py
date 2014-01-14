#!/usr/bin/python
import os
import re
import csv
import logging
import gzip
import re

#loggin setup
logging.basicConfig(filename="findUserStats.log", filemode="a", level=logging.INFO, format="[ %(asctime)s ] %(levelname)s : %(message)s")

saida = open("findUsersStats.txt","w")

#build header
for arq in os.listdir("./profiles"):
	try:
      		logging.info("["+arq+"]:  iniciando" )

		profilePage = gzip.open('./profiles/'+arq+'/profile',"r").read()

		description = re.findall('<meta property="pinterestapp:about" name="pinterestapp:about" content="(.*)" data-app="">',profilePage)[0].strip().replace("'", r"\'")
		nBoards= re.findall('<meta property="pinterestapp:boards" name="pinterestapp:boards" content="(.*)" data-app="">',profilePage)[0].strip()
		nFollowing = re.findall('<meta property="pinterestapp:following" name="pinterestapp:following" content="(.*)" data-app="">',profilePage)[0].strip()
		nFollowers = re.findall('<meta property="pinterestapp:followers" name="pinterestapp:followers" content="(.*)" data-app="">',profilePage)[0].strip()
		nPins= re.findall('<meta property="pinterestapp:pins" name="pinterestapp:pins" content="(.*)" data-app="">',profilePage)[0].strip()
		nLikes = re.findall('<a href="/'+arq+'/likes/">\n.*\n(.*)',profilePage)[0].strip().split()[0].strip()

		saida.write("update users set pinterestDesc='"+str(description)+"', nPinsLifeTime='"+str(nPins)+"', nBoardsLifeTime='"+str(nBoards) +"', nLikesLifeTime='"+str(nLikes)+"', nFollowersPinterest='" +str(nFollowers)+"', nFollowingPinterest='"+str(nFollowing)+"' where pinterestID='" +str(arq)+"'" + "\n")


	except Exception, e :
      		logging.error("["+ arq+"]: "+str(e))
