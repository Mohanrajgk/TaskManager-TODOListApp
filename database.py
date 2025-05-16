# Import your Todo model (assumed to be Pydantic)
from model import Todo
#Mongodb async driver
import motor.motor_asyncio

# MongoDB connection setup
client = motor.motor_asyncio.AsyncIOMotorClient('mongodb://localhost:27017')
database = client.TodoList
collection = database.todo

# Fetch a single Todo item by title
async def fetch_one_todo(title):
    document = await collection.find_one({"title": title})
    return document 

# Fetch all Todos from the collection
async def fetch_all_todos():
    todos = []
    cursor = collection.find({})
    async for document in cursor:
        todos.append(Todo(**document))
    return todos 

# Insert a new Todo into the database
async  def create_todo(todo):
   document = todo
   result = await collection.insert_one(document)
   return document

# Update a Todo by title
async def update_todo(title, desc):
   await collection.update_one({"title":title},{"$set":{"description":desc}})
   document = await collection.find_one({"title":title})
   return document

# Delete a Todo by title
async  def  remove_todo(title):
   await collection.delete_one({"title":title})
   return True

