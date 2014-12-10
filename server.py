from bottle import route, request, run
import csv

csvfile = open('machines.csv', "wb")
fieldnames = ['host', 'file', 'hash']
csvwriter = csv.DictWriter(csvfile, fieldnames)
csvwriter.writeheader()

@route('/data', method='POST')
def writedata():

    try:
        csvwriter.writerow(request.json)
    except:
        pass

run(server="tornado")