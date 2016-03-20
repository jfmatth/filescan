import os
import hashlib
import socket
import json
import requests
import argparse
from argparse import Action


def hostname():
    return socket.gethostname()

def hashfile(afile, blocksize=8192):
    hasher=hashlib.md5()

    file = open(afile, "rb")
    while True:
        data = file.read(blocksize)
        if not data:
            break
        hasher.update(data)

    file.close()
    return hasher.hexdigest()

def logresult(data=None, url=None):
    if data and type(data) == dict:
        if url:
            if url == "db":
                try:
                    File.create(**data)
                    print data['file']
                except:
                    pass

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
                    raise



if __name__== "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-U", "--url", help="URL of http server receiving data", type=str)
    parser.add_argument("-P", "--path", help="Path to scan", type=str)

    args = parser.parse_args()
    print args

    scan(url=args.url, path=args.path)
