import time

from fastapi import FastAPI

app = FastAPI()

@app.get("/generate")
async def root():
    time.sleep(15)
    return {"message": "New message"}