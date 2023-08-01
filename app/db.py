from sqlalchemy import create_engine
from pymongo import MongoClient

# Postgres
engine = create_engine("postgresql://user:password@localhost:5432/mydatabase")

# Mongo
client = MongoClient("mongodb://localhost:27017/")
