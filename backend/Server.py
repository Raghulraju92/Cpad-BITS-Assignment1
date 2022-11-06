
from flask import Flask,jsonify,request
from mysqlhandler import dbhandler
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

db = dbhandler()

@app.route('/getstudentdetails/',methods=['GET'])
def getstudentdetails():
    res = db.getstudentsdata()
    return jsonify(res)


@app.route('/getdrivedetails/',methods=['GET'])
def getdrivedetails():
    res = db.getdrivedata()
    return jsonify(res)

@app.route('/getuserdetails/',methods=['POST'])
def getuserdetails():
    res = db.getusersdata()
    return jsonify(res)

@app.route('/updatestudentdetails/',methods=['POST'])
def updatestudentdetails():
    data = request.get_json()
    res = db.updatestudentsdata(data['student'])
    return jsonify(res)

@app.route('/updatedrivedetails/',methods=['POST'])
def updatedrivedetails():
    data = request.get_json()
    res = db.updatedrivedata(data['drive'])
    return jsonify(res)

@app.route('/insertstudentdetails/',methods=['POST'])
def insertstudentdetails():
    data = request.get_json()
    res = db.insertstudentdata(data['students'])
    return jsonify(res)

@app.route('/insertdrivedetails/',methods=['POST'])
def insertdrivedetails():
    data = request.get_json()
    res = db.insertdrivedata(data['drive'])
    return jsonify(res)

@app.route('/insertuserdetails/',methods=['POST'])
def insertuserdetails():
    data = request.get_json()
    res = db.insertuserdetails(data['users'])
    return jsonify(res)

@app.route('/authentication/',methods=['POST'])
def authentication():
    data = request.get_json()
    res = db.authenticate(data['userdetail'])
    return jsonify(res)

@app.route('/getcounts/',methods=['GET'])
def getcounts():

    res = db.getcounts()
    return jsonify(res)


if __name__ == '__main__':
 
    app.run(host='0.0.0.0',port=5000)