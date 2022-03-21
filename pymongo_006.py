import pymongo
import time

index = 1
client = pymongo.MongoClient("localhost",27017)
db = client["imdb"]
col = db["title.basics"]

while True:
        movie_title = input("input movie name:")

        pipeline = [
                    {"$match":
                        {"primaryTitle":{"$regex":(movie_title),'$options' : 'i'}}},
                    {"$lookup":
                        {"from":"title.ratings","localField":"tconst","foreignField":"tconst","as":"rating"}},
                    {"$unwind":"$rating"},
                    {"$project":{"startYear":1,"primaryTitle":1,"rating.averageRating":1,"_id":0}}]

        for doc in col.aggregate(pipeline):

            print(doc)
            time.sleep(1)

