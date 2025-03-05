from flask import Flask, jsonify, request
from pymongo import MongoClient
from bson import ObjectId
import datetime

app = Flask(__name__)

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017")
db = client["inventoryDB-W1"]
collection = db["audits"]

# Get all audit records
@app.route('/api/audits', methods=['GET'])
def get_audits():
    audits = list(collection.find({}, {"_id": 1, "item_name": 1, "warehouse": 1, "quantity": 1, "status": 1, "audit_date": 1}))
    for audit in audits:
        audit["_id"] = str(audit["_id"])  # Convert ObjectId to string
    return jsonify(audits)

# Add new audit record
@app.route('/api/audits', methods=['POST'])
def add_audit():
    data = request.json
    data["audit_date"] = datetime.datetime.utcnow()  # Add timestamp
    result = collection.insert_one(data)
    return jsonify({"message": "Audit added successfully", "id": str(result.inserted_id)}), 201

if __name__ == '__main__':
    app.run(debug=True)
