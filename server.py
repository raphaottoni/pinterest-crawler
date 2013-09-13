#!/usr/bin/python

import crawlLib
import sys
import socket
import json
import datetime
import os.path
import pinterest


#def getIdNotFetched():
#  for dirname, dirnames, filenames in os.walk('profiles_to_crawl/'):
#    for profileId in dirnames:
#      if ( (not os.path.exists(os.path.join(dirname, profileId)+"/fetched0")) and  (not os.path.exists(os.path.join(dirname, profileId)+"/fetched1"))):
#         return profileId

#from googleplus import *
# Get list of files to collect
#files_all = set([a.rstrip() for a in open("%s/files_all.txt" % (LOGS_DIR))])
#files_collected = set([a.rstrip().split(" ")[0] for a in open("%s/files_collected.txt" % (LOGS_DIR))])
#files_available = sorted(list((files_all - files_collected)), reverse=True)

PORT=7777
BUFSIZE=10240
pinterest = pinterest.Pinterest()

# Startup server
clients = [None]
server = socket.socket()
server.bind(("", PORT))
server.listen(socket.SOMAXCONN)

while True:
    client, client_addr = server.accept()
    message_text = client.recv(BUFSIZE)
    try:
        message = json.loads(message_text)
        command = message["command"]
        if command == "GET_LOGIN":
            client_id = len(clients)
            client_host = socket.gethostbyaddr(client_addr[0])[0]
            client_pid = message["processid"]
            clients.append([client_host, client_pid, 0, None, None])
            client.send(json.dumps({"command": "GIVE_LOGIN", "clientid": client_id}))
            print "Quer me pegar: %s" % client_id
        elif command == "GET_ID":
            print "Recebi comando GetID"
            profileId = pinterest.getIDtoCrawl()
            #profileId = "raphaottoni"
            #profileId = "gslth"
            #profileId = "mufan2"
            #profileId = "eatsleepwear"
            #profileId = "2minlaundry"
            #profileId = "1linds"
            #profileId = "camicado"
            profileId = "raphaottoni"
            #print profileId
            client.send(json.dumps({"command": "GIVE_ID", "profileID": str(profileId)}))
            client_id = message["clientid"]
            clients[client_id][2] += 1
            clients[client_id][3] = datetime.datetime.today()
            clients[client_id][4] = profileId
            pinterest.statusColeta(profileId,'1',clients[int(client_id)][0])
        elif command == "DONE_ID":
            client_id = message["clientid"]
            print client_id
            if ( message["status"] == 0):
              pinterest.statusColeta(client_id,'2',clients[int(message["crawlerID"])][0])
            else:
              pinterest.statusColeta(client_id,'-2',clients[int(message["crawlerID"])][0])
            print "Terminou " + client_id+ " - Status " + str(message["status"])
        elif command == "GET_STATUS":
            status_text = ":::::::::: Result ::::::::::\n"
            for i, client_info in enumerate(clients):
                if client_info is not None:
                    status_text += "  #%d - %s/%s (%d at %s, %s) [%s]\n" % (i, client_info[0], client_info[1], client_info[2], client_info[3].strftime("%Y-%m-%d %H:%M:%S"), str(datetime.datetime.today() - client_info[3]), client_info[4])
            client.send(json.dumps({"command": "GIVE_STATUS", "status": status_text}))
       # elif command == "GIVE_NEWIDS":
       #      id_list = message["idlist"]
       #      for new_id in id_list:
       #          if new_id not in files_collected:
       #              files_available.append(new_id)
       # else:
       #     client.send(json.dumps({"command": "ERROR"}))
    except Exception, error:
      print "Client ERROR: %s" % (str(error))
      client.send(json.dumps({"command": "ERROR"}))
      client.close()
