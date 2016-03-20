from bottle import route, request, run

from db import filescan

@route('/file', method='POST')
def writedata():
    try:
        filescan.create(host = request.json["host"],
                        path = request.json["file"],
                        hash = request.json["hash"])
    except:
        print "error on writer"

run(host='0.0.0.0', port=8080)
