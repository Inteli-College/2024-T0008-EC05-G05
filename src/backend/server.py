from fastapi import FastAPI
from routers import *

# Create the FastAPI app

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World!"}


app.include_router(dashboard_api, prefix="/dashboard_api")