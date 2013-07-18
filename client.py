#!/usr/bin/python
import os
import sys
import datetime
import socket
import json
import time
import crawlLib

PORT=7777
BUFSIZE=10240
try:
    HOST = sys.argv[1]
except:
    sys.exit("USAGE: ./%s [server_address]" % (sys.argv[0]))

#Create a collector
crawler = crawlLib.Crawler()

# Client login into the server
process_id = os.getpid()
server = socket.socket()
server.connect((HOST, PORT))
server.send(json.dumps({"command": "GET_LOGIN", "processid": process_id, "clientid": 0}))
message = json.loads(server.recv(BUFSIZE))
client_id = message["clientid"]
server.close()
print "Server gave me this id: %s " % client_id
n_ok = 0
n_total = 0
ACTIVE = True
errorFlag = False
while ACTIVE:
    try:
        server = socket.socket()
        server.connect((HOST, PORT))
        print "enviando Comando de pega ID"
        server.send(json.dumps({"command": "GET_ID", "clientid": client_id}))
        message = json.loads(server.recv(BUFSIZE))
        command = message["command"]
        print "Recebi command"
        server.close()
        if command == "GIVE_ID":
            profileID = message["profileID"]
            print profileID
            resposta = crawler.gatherInfo(profileID)
            server = socket.socket()
            server.connect((HOST, PORT))
            if (resposta == 0):
              server.send(json.dumps({"command": "DONE_ID", "clientid": profileID, "status": 0, "crawlerID": client_id}))
            else:
              server.send(json.dumps({"command": "DONE_ID", "clientid": profileID, "status": 1,"crawlerID": client_id}))

            server.close()
        elif command == "FINISH":
            ACTIVE = False

    except Exception, e:
        print "Deu pau---" + str(e)
        errorFlag= True
        #error_file = open("%s/client_error%s.txt" % (save_dir, client_id), "a+")
        #error_file.write("[%s] (%s): %s\n" % (str(datetime.datetime.today()), file_to_collect, str(e)))
        #error_file.close()
