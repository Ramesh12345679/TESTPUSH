import pymongo
client = pymongo.MongoClient("mongodb+srv://nagamani:<nagamani>@cluster0.ntzg6.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)
d = {
    "name" : "ramesh",
    "email": "ram@gmail.com",
    "surname": "rb"
}
db1 = client['mongotest']
coll = db1['test']
print("hi git ")

