import pymongo
import time

index = 1
client = pymongo.MongoClient("localhost",27017)
db = client.imdb
for item in db.title.basics.find({"startYear":2020}):
        print(index)
        print(item)
        time.sleep(1)
        index+=1
