import pymongo
client = pymongo.MongoClient("localhost",27017)
db = client.imdb
fields_list_1 = ["startYear","primaryTitle","isAdult","runtimeMinutes"]
fields_list_2 = ["birthYear","deathYear","primaryName"]

query_object = input("Query on 1 for Movie or 2 for Person:")

if query_object == "1":
    collection = "name.basics";
else: 
    if query_object == "2":
        collection = "title.basics";

start_year = input("Year of Movie:")
title = input("Name of Movie:")
is_adult = input("1 for Adult, 0 for normal:")
time_minutes = input("Time of Movie in minutes:")



for item in db.collection.find({"fields_list_" + str(query_object)[0]:start_year}):
        print(item)
