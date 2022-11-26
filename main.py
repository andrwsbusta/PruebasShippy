import pymongo
from flask import Flask
from flask_cors import CORS
from flask import jsonify
from flask import request
import json
from waitress import serve
app = Flask(__name__)
cors = CORS(app)
MiGestor = pymongo.MongoClient("mongodb+srv://admin-staging:J3QUMICMQE9T3vnl@dropshipping-staging.6meionj.mongodb.net/mongo-dropshipping-staging?authSource=admin")
MiDB = MiGestor["mongo-dropshipping-staging"]
MiColec = MiDB["shippingOrders"]
@app.route("/guide/<string:numGui>/status/<string:statusFin>",methods=['PUT'])
def modificarShippyOrder(numGui,statusFin):
    busca = MiColec.find_one({"guides":numGui})
    if busca is not None:
        modifica = MiColec.update_one({"guides": numGui}, {"$set": {status: statusFin}})
    else:
        return print('no se encuentra la guia')

    return jsonify(modifica)
@app.route("/",methods=['GET'])
def loadFileConfig():
    with open('config.json') as f:
        data = json.load(f)
    return data
if __name__=='__main__':
    dataConfig = loadFileConfig()
    print("Server running : "+"http://"+dataConfig["url-backend"]+":" + str(dataConfig["port"]))
    serve(app,host=dataConfig["url-backend"],port=dataConfig["port"])



