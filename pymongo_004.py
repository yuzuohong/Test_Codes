import pymongo
import time
import re

index = 1
client = pymongo.MongoClient("localhost",27017)
db = client["imdb"]
col = db["title.basics"]

#find_statement = {"titleType":"movie","genres":re.compile("Mystery|Drama|Crime|Comedy|Horror"),"startYear":{"$gt":1980},"runtimeMinutes":{"$gt":90}},{"startYear":1,"primaryTitle":1,"genres":1,"_id":0,"runtimeMinutes":1}

sort = "startYear"

find_statement = {"titleType":"movie","startYear":{"$gt":2000},"runtimeMinutes":{"$gt":90},"genres":re.compile("Mystery|Drama|Crime|Comedy|Horror" )}

output_fields = {"startYear":1,"primaryTitle":1,"genres":1,"_id":0,"runtimeMinutes":1}

record_list = col.find(find_statement,output_fields)

record_count = col.count_documents(find_statement)

#for item in db.title.basics.find({"titleType":"movie","genres":re.compile("Mystery|Drama|Crime|Comedy|Horror"),"startYear":{"$gt":1980},"runtimeMinutes":{"$gt":90}},{"startYear":1,"primaryTitle":1,"genres":1,"_id":0,"runtimeMinutes":1}):

for item in record_list.sort(sort,1):
        print("no." + str(index) + " of " + str(record_count))
        print(item)
        time.sleep(0.5)
        index+=1
