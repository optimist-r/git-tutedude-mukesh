from flask import request
from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["todoDB"]
collection = db["items"]

@app.route('/submittodoitem', methods=['POST'])
def submit_todo():
    itemName = request.form.get("itemName")
    itemDescription = request.form.get("itemDescription")

    collection.insert_one({
        "itemName": itemName,
        "itemDescription": itemDescription
    })

    return {"message": "Item added successfully"}, 201
