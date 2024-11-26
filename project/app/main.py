from fastapi import Depends, FastAPI

app = FastAPI()


@app.get("/ping")
async def pong():
    return {"ping": "pong!"}
