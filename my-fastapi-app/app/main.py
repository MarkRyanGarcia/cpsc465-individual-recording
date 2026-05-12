from fastapi import FastAPI
from mangum import Mangum

app = FastAPI(title="my-fastapi-app")


@app.get("/")
async def root():
    return {"message": "Hello World!"}



@app.get("/endpoint2")
async def endpoint2():
    return {"message": "Hello from endpoint 2!"}



handler = Mangum(app, lifespan="off")
