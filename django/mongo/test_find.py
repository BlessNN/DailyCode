#from pymongo import MongoClient
import pymongo

client = pymongo.MongoClient()
db = client.test

cur = db.test.find().sort([ ("deal_date", pymongo.ASCENDING)])
#cur = db.test.find()
for doc in cur:
	for d in doc:
		print(str(d) + " : "+str(doc[d]))


