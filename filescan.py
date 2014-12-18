import os
import hashlib
import socket
import json
import requests
import argparse
from argparse import Action

from filescan_peewee import File, db

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


def logresult(data=None, url=None):
    if data and type(data) == dict:
        # print it out and post to server
        
        if url:
            if url == "db":
                File.create(**data)
                print ".",
            else:
                try:
                    headers = {'Content-Type': 'application/json'}
                    r = requests.post(url, data=json.dumps(data), headers=headers)
                    print("%s" % r.status_code),
                except:
                    pass
        else:
            print data
        
def scan(url=None, path=None):
    hn = hostname()
    
    if path == None:
        sp = os.path.dirname(os.path.abspath(__file__))
    else:
        sp = os.path.abspath(path)
        
    for root, dirs, files in os.walk(sp):
                    
        for f in files:
            fullpath = os.path.normcase(os.path.normpath(os.path.join(root,f) ) ) 
    
            if os.path.isfile(fullpath):
                try:
                    data = {'host':hn, 
                            'file':fullpath,
                            'hash':hashfile(fullpath),
                            }
                    
                    logresult(data, url)
                    
                except KeyboardInterrupt:
                    raise
                
                except:
                    print "exception %s" % fullpath
                
        
        
if __name__== "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-U", "--url", help="URL of http server receiving data", type=str)
    parser.add_argument("-P", "--path", help="Path to scan", type=str)
    
    args = parser.parse_args()
    print args
    
    scan(url=args.url, path=args.path)

    