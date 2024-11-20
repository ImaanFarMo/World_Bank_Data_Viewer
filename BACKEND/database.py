import motor.motor_asyncio
from model import WorldBank
from bson import ObjectId 
from fastapi import FastAPI, HTTPException
client = motor.motor_asyncio.AsyncIOMotorClient('mongodb://localhost:27017/')
database = client.WorldBankList
collection = database.worldbank

# get one country's information
async def fetch_one_data(country_name):
    document = await collection.find_one({"country_name": country_name})
    return document

# get all countries information 
async def fetch_all_datas():
    #todos = []
    banks = []
    async for document in collection.find({}):
        banks.append(document)
       
    return banks

# create a new country 
async def create_data(worldbank):
    document = worldbank
    result = await collection.insert_one(document)
    return document


# update a country 
async def update_data(country_name, population, gdp, gdp_per_capita, unemployment_rate):
    await collection.update_one({"country_name": country_name}, {"$set": {"population":population, "gdp":gdp, "gdp_per_capita": gdp_per_capita, "unemployment_rate":unemployment_rate
                                                                           }})
    document = await collection.find_one({"country_name": country_name})
    return document

# remove a country 
async def remove_data(country_name):
    await collection.delete_one({"country_name": country_name})
    return True