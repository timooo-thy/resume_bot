from fastapi import FastAPI
from time import time

app = FastAPI()


@app.get("/")
async def main():
    return {"message": "Welcome to the Resume Bot API"}


@app.get("/health")
async def health_check():
    return {"status": "healthy", "timestamp": time()}
