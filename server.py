from bottle import route, request, run
import csv
import argparse
from argparse import Action


csvfile = open('machines.csv', "wb")
fieldnames = ['host', 'file', 'hash']
csvwriter = csv.DictWriter(csvfile, fieldnames)
csvwriter.writeheader()

@route('/file', method='POST')
def writedata():

    try:
        csvwriter.writerow(request.json)
    except:
        print "error on writer"

parser = argparse.ArgumentParser()
parser.add_argument("-L", "--local", help="Run local HTTP server, otherwise Tornado", action="store_true")
args = parser.parse_args()
print args

if args.local:
    run(host='localhost', port=8080)
else:
    run(server="tornado")

