import pymongo

client = pymongo.MongoClient(
    'mongodb+srv://betote:6hBzndMr3RLsBDFx@cluster0-3vp2d.mongodb.net/test?retryWrites=true&w=majority&ssl_cert_reqs=CERT_NONE')
db = client.test

def getDBconnection():
    return db

def updateBlockchain(chain):
    collection = db.blockchain
    for index in range(len(chain)):
        block =  chain[index]
        exists = collection.find({"hash": block["hash"]}).count()
        if block["index"] == 0 and exists == 0:
            collection.insert_one(block)
        elif exists == 0:
            previous_hash = chain[index - 1]["hash"]
            if block["previous_hash"] == previous_hash:
                collection.insert_one(block)
            else:
                return False
    return True

def getBlockchain():
    collection = db.blockchain
    chain = []
    for block in collection.find():
        del block["_id"]
        chain.append(block)
    return {"chain" : chain}
