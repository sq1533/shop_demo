from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

@app.get("/")
async def go():
    pass

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8080)