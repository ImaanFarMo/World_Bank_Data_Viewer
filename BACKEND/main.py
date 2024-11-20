

from fastapi import FastAPI, HTTPException
from typing import List
from model import WorldBank

from database import (
    fetch_one_data,
    fetch_all_datas,
    create_data,
    update_data,
    remove_data,
)


from fastapi.middleware.cors import CORSMiddleware
app = FastAPI()

origins = [
    "http://localhost:3000",
]#

# what is a middleware? 
# software that acts as a bridge between an operating system or database and applications, especially on a network.

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def read_root():
    return {"Hello": "World"}


#calls t oreturn a list of todos
@app.get("/api/worldbank/", response_model=List[WorldBank])
async def get_all_data():
    response = await fetch_all_datas()
    if response:
        return response
    raise HTTPException(404, "No countries found")



#calls to get a single todo item
@app.get("/api/worldbank/{country_name}", response_model=WorldBank)
async def get_data_by_name(country_name):
    response = await fetch_one_data(country_name)
    if response:
        return response
    raise HTTPException(404, f"There is no todo with the title {country_name}")

    from fastapi import FastAPI, HTTPException
from pymongo import MongoClient




#creates a new todo item by calling create_todo(todo.dict)
@app.post("/api/worldbank/", response_model=WorldBank)
async def post_data(worldbank: WorldBank):
    response = await create_data(worldbank.model_dump())
    if response:
        return response
    raise HTTPException(400, "Something went wrong")



@app.put("/api/worldbank/{country_name}/", response_model=WorldBank)
async def put_data(country_name: str, population: int, gdp: float, gdp_per_capita: float, unemployment_rate: float):
    response = await update_data(country_name, population ,gdp, gdp_per_capita, unemployment_rate)
    if response:
        return response
    raise HTTPException(404, f"There is no country with the name {country_name} in the list")




if __name__ == "__main__":
    app.run(debug=True)
#deleted a todo item by calline remove_todo(title)
@app.delete("/api/worldbank/{country_name}")
async def delete_data(country_name):
    response = await remove_data(country_name)
    if response:
        return "Successfully deleted country"
    raise HTTPException(404, f"There is no country with the name {country_name}")