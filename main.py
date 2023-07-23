from pymongo import MongoClient
#replace <uri> with your MongoDB Atlas connection string
uri = "mongodb+srv://Dakshi:Dyh9599@cluster0.qvy5xhm.mongodb.net/"
client = MongoClient(uri)
#replace <database-name> with the name of your database
db = client["webapp"]
#replace <collection-name> with the name of your database
collection =db["MongoDB"]

#click the connection
try:
    client.admin.command("ping")
    print("Pinged your deploymnt.You successfully connected to MongoDB")
except Exception as e:
    print(e)

document = {"name": "Daniel","age":36}

#insert the document into the collection
insert_result = collection.insert_one(document)

#print the ID of the inserted document
print("Inserted Document ID",insert_result.inserted_id)

client.close()