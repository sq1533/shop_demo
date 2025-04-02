from fastapi import FastAPI, Depends

app = FastAPI()

@app.get("/goSignUp")
async def signUpUser():
    pass

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8080)