import os
import json
import pymongo
from flask import Flask
from flask import request
from flask_cors import CORS
app = Flask(__name__)
# usr = os.environ['MONGO_DB_USER']
# pwd = os.environ['MONGO_DB_PASS']
app = Flask(__name__)
CORS(app)

client = pymongo.MongoClient("mongodb://localhost:27017/" + "@firstcluster-obuqd.mongodb.net/test?retryWrites=true&w=majority")
db = client['workingwage']
collection1 = db['us coordinates']

@app.route("/", methods=['POST'])
def insert_document():
    req_data = request.get_json()
    collection1.insert_one(req_data).inserted_id
    return ('', 204)

@app.route('/')
def get():
    documents = collection1.find()
    response = []  
    for document in documents:
        document['_id'] = str(document['_id'])
        response.append(document)
    return json.dumps(response)
if __name__ == '__main__':
    app.run()