import os
import sys
import hashlib
import socket
import json
import requests

URL="http://localhost:8080/data"

def hostname():
    return socket.gethostname() 

def hashfile(afile, hasher=hashlib.md5(), blocksize=65536):

    f = open(afile,"rb")
    
    buf = f.read(blocksize)
    while len(buf) > 0:
        hasher.update(buf)
        buf = f.read(blocksize)

    f = None
    return hasher.hexdigest()


def logresult(data=None):
    if data and type(data) == dict:
        # print it out and post to server
        
        if URL:
            try:
                headers = {'Content-Type': 'application/json'}
                requests.post(URL, data=json.dumps(data), headers=headers)
                print("."),
            except:
                pass
        else:
            print data
        
def scan(path=None):
    hn = hostname()
    
    if path == None:
        sp = os.path.dirname(os.path.abspath(__file__))
        
    for root, dirs, files in os.walk(sp):
                    
        for f in files:
            fullpath = os.path.normcase(os.path.normpath(os.path.join(root,f) ) ) 
    
            if os.path.isfile(fullpath):
                data = {'host':hn, 
                        'file':fullpath,
                        'hash':hashfile(fullpath)
                        }
                
                logresult(data)
                
        
if __name__== "__main__":
    scan()
    