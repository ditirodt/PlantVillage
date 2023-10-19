from fastapi import FASTAPI

app = FastAPI()

@app.get("/ping")
async def ping():
    return "Hello, I am alive"
