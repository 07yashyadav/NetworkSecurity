from pymongo import MongoClient

uri = "mongodb+srv://yashthibgoan_db_user:Yash123@cluster0.sqcjvfx.mongodb.net/?retryWrites=true&w=majority"

client = MongoClient(uri, tls=True)

client.admin.command("ping")

print("✅ Connected successfully")