
from flask import Flask,jsonify,request
from Database.mysqlhandler import dbhandler
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

db = dbhandler()

@app.route('/getstudentdetails/',methods='POST')
def getstudentdetails():
    res = db.getstudentsdata()
    return jsonify(res)


@app.route('/getdrivedetails/',methods='POST')
def getdrivedetails():
    res = db.getdrivedata()
    return jsonify(res)


@app.route('/updatestudentdetails/',methods='POST')
def updatestudentdetails():
    data = request.get_json()
    res = db.updatestudentsdata(data['student'])
    return jsonify(res)

@app.route('/updatedrivedetails/',methods='POST')
def updatedrivedetails():
    data = request.get_json()
    res = db.updatedrivedata(data['drive'])
    return jsonify(res)

@app.route('/insertstudentdetails/',methods='POST')
def insertstudentdetails():
    data = request.get_json()
    res = db.insertstudentdata(data['students'])
    return jsonify(res)

@app.route('/insertdrivedetails/',methods='POST')
def insertdrivedetails():
    data = request.get_json()
    res = db.insertdrivedata(data['drive'])
    return jsonify(res)                



if __name__ == '__main__':
 
    app.run(host='localhost',port=5000)