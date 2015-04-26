import json
from pymongo import MongoClient
import string

client = MongoClient('localhost', 27017)
db = client['egillkrona']
collection = db['barcode']

kaupdb = client['hagkaup']
hagcollection = db['gosdrykkir']

for doc in collection.find():

    name = doc['name']
    name = name.rstrip(".")
    name =name.replace("-", " ")
    name = name.replace("0,5", "500m")
    name = (name.replace("ltr", "l").replace("Ltr", "l").replace("LTR", "l"))
    name = name.replace("=", "")
    name = name.replace("1L", "1l").replace("1 l", "1l")
    name = name.replace("33cl", " 330ml").replace("33CL", " 330ml").replace("33 cl", " 330ml")
    name = name.replace("1/2 l", "500ml")

    name = name.replace(".", " ")
    name = name.replace("+", " ")
    #print(name)
    name = name.replace(" l", "l")
    name = name.replace("1/2l", " 500ml")
    name = name.replace("1/2L", " 500ml")
    name = name.replace("1/2 L", " 500ml")
    name = name.replace("1/2", " 500ml")

    name = name.replace("x2", " x 2")
    name = name.replace("x1", " x 1")
    name = name.replace(" 4x", " 4 x")


    name = name.replace(" 1/4l", " 250ml")
    name = name.replace("1/4", "250ml")

    name = name.replace(" sl", " 960ml")
    name = name.replace(" SL", " 960ml")

    name = name.replace("   ", " ")
    name = name.replace("  ", " ")

    name = name.replace("Mexlime", "Mexican Lime") # FIX FOR MEX LIME FUCKUP

    #print(doc['name'], "*****")
    name = name[:-1] + name[-1].lower()
    #print(name)
    #print(doc['_id'])

for doc in hagcollection.find():
    print(doc[''])
