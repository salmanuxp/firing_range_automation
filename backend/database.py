from models import Log
import motor.motor_asyncio

# define the mongodb server route
client = motor.motor_asyncio.AsyncIOMotorClient('mongodb://localhost:27017')

# select database and collection name
database = client.thesis
collection = database.logs


# create the actions

# create-a-log-entry
async def create_log(log):
    document = log
    result = await collection.insert_one(document)
    return document