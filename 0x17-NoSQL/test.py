import bottle
from pymongo import MongoClient
import pprint

client = MongoClient()
db = client.rptutorials
print(client)

tutorial = db.tutorial

tutorial1 = {
     "title": "Working With JSON Data in Python",
     "author": "Lucas",
     "contributors": [
         "Aldren",
         "Dan",
         "Joanna"
 ],
     "url": "https://realpython.com/python-json/"
}

tutorial2 = {
     "title": "Python's Requests Library (Guide)",
     "author": "Alex",
     "contributors": [
         "Aldren",
         "Brad",
         "Joanna"
     ],
     "url": "https://realpython.com/python-requests/"
}

tutorial3 = {
     "title": "test 's Requests Library (Guide)",
     "author": "Alex",
     "contributors": [
         "Aldren",
         "Brad",
         "Joanna"
     ],
     "url": "https://realpython.com/python-requests/"
}

result = tutorial.insert_many([tutorial1, tutorial2, tutorial3])
print(result)

jon_tutorial = tutorial.find_one({"author": "Lucas"})
pprint.pprint(jon_tutorial)
client.close()
