#!/usr/bin/env python3

from pymongo import MongoClient
import sys,re

if not len(sys.argv) == 2:
    print ("Usage: " + sys.argv[1] + "<target>")
    exit()

ip = sys.argv[1]

try:
    client = MongoClient(ip,27017,connectTimeoutMS=1000,socketTimeoutMS=1000,waitQueueTimeoutMS=1000)
    server_info = client.server_info()
    print(server_info)
except KeyboardInterrupt:
    print("Interrupted by user. Exiting...")
    exit()
except Exception (e):
    print(e)
    pass
