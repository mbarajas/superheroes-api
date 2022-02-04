from fastapi import FastAPI
from app.api.routes import api_router

app = FastAPI()
app.include_router(api_router)

@app.get("/")
async def root():
    return {"message": "Welcome to the Superhero API"}
