from fastapi import FastAPI, Depends, Request, HTTPException, HTMLResponse
from fastapi.templating import Jinja2Templates
from shop_demo.api.schema import *

# Fast API app 정의
app = FastAPI()

# HTML templates, jinjaTemplates
templates = Jinja2Templates(directory="/templates/")

# mainHome 진입
@app.get("/", response_class=HTMLResponse)
async def home(request:Request):
    return templates.TemplateResponse("mainPage.html",{"request":request})

@app.post("/goSignUp/", response_model=userOut)
async def signUpUser(user:userIn):
    if user.email == None:
        raise HTTPException(status_code=400, detail="이메일 주소를 입력해주세요.")
    return {"email":f"{user.email} 환영합니다."}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8080)