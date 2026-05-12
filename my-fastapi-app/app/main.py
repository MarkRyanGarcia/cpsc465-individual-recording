from fastapi import FastAPI
from mangum import Mangum

app = FastAPI(title="my-fastapi-app")


@app.get("/")
async def root():
    return {"message": "Hello World!"}



handler = Mangum(app, lifespan="off")
