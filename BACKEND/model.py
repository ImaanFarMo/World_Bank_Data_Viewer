from pydantic import BaseModel



from fastapi import FastAPI, HTTPException

#database
class WorldBank(BaseModel):
    country_name: str
    population: int
    gdp: float
    gdp_per_capita: float
    unemployment_rate: float



    
