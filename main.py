from typing import Collection
import pymongo

url= "mongodb://127.0.0.1:27017"
client=pymongo.MongoClient(url)
database=client['mylib']
collection=database['books']

books=[books for books in collection.find({})]

print(books)