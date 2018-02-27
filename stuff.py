import pymongo
import json

def setup():
    connection = pymongo.MongoClient('homer.stuy.edu')
    connection.drop_database("cosh")
    db = connection.cosh
    collection = db.complaints
    data = json.load(open("views.json"))
    collection.insert_many(data)

#setup()

def query_name(name):
    connection = pymongo.MongoClient('homer.stuy.edu')
    db = connection.cosh
    collection = db.complaints
    c = collection.find( { "name": name }, {"name":1, "_id": 0, "description":1, "owner.displayName":1})
    complaints = []
    for x in c:
        complaints += [x]
    return complaints

def query_download_count(count):
    c = collection.find( {"downloadCount": count} )
    for x in c:
        print x
        #print "found " + str(count)
    
def query_owner(name):
    c = collection.find({ "owner.displayName": name })
    for x in c:
        print x
        #print "found " + name

def query_table_owner(name):
    c = collection.find({ "tableAuthor.displayName": name})
    for x in c:
        print x
        #print "found " + name

def query_tag(tag):
    c = collection.find({"tags": tag })
    for x in c:
        print x
        #print "found " + tag

def get_names():
    connection = pymongo.MongoClient('homer.stuy.edu')
    db = connection.cosh
    collection = db.complaints
    c = collection.find({}, {"name":1, "_id": 0})
    complaints = []
    for comp in c:
        complaints += [comp["name"]]
    return complaints

'''      
query_name("Survey of Credit Card Plans")
query_download_count(1449)
query_owner("ming")
query_table_owner("Doug Taylor")
query_tag("credit cards")
setup()
get_names()
'''
