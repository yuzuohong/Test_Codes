import pymongo
import time

index = 1
client = pymongo.MongoClient("localhost",27017)
db = client.imdb
for item in db.title.basics.find({"titleType":"movie","$or":[{"genres":{"$regex":"Mystery"}},{"genres":{"$regex":"Drama"}},{"genres":{"$regex":"Crime"}},{"genres":{"$regex":"Comedy"}},{"genres":{"$regex":"Horror"}}],"startYear":{"$gt":1980},"runtimeMinutes":{"$gt":90}}):
        print(index)
        print(item)
        time.sleep(2)
        index+=1
