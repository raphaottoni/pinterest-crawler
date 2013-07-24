#!/usr/bin/python

import os
import sys
import socket
import json

#from googleplus import PORT
#from googleplus import BUFSIZE
#from googleplus import LOGS_DIR

PORT = 7777
BUFSIZE=10240

try:
    HOST = sys.argv[1] 
except:
    HOST = "localhost"

print "HOST = %s\n" % (HOST)

process_id = os.getpid()
server = socket.socket()
server.connect((HOST, PORT))
server.send(json.dumps({"command": "GET_STATUS", "clientid": 0}))
#server.send("")
message = json.loads(server.recv(BUFSIZE))
server.close()
#
if message["command"] == "GIVE_STATUS" :
    print message["status"] 
#else:
#    print message["command"]
