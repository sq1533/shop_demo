from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from contextlib import asynccontextmanager

import firebase_admin
from firebase_admin import credentials, firestore

from config import settings

@asynccontextmanager
async def lifespan(app : FastAPI):
    try:
        cred_path = settings.FIREBASE_SERVICE_ACCOUNT_PATH
        cred = credentials.Certificate(cred_path)

        firebase_admin.initialize_app(cred)
        app.state.db = firestore.client() #request.app.state.db 접근
        print('Firebase Admin SDK 초기화')
    except ValueError as e:
        print(f'실패 : {e}')
    except FileNotFoundError:
        print(f'키 오류 경로: {cred_path}')
    yield

app = FastAPI(title='antioch', version='0.1.0', lifespan=lifespan) # docs_url, redoc_url 보안을 위해 추후 비활성화

templates = Jinja2Templates(directory='templates')

mock_db_items = {
    1: {"name": "클래식 스니커즈", "price": 65000, "description": "어디에나 잘 어울리는 기본 아이템입니다."},
    2: {"name": "가죽 백팩", "price": 120000, "description": "노트북 수납이 가능한 튼튼한 가방입니다."},
    3: {"name": "볼캡 모자", "price": 35000, "description": "자외선 차단에 필수적인 패션 모자입니다."}
}

@app.get('/', response_class=HTMLResponse)
async def read_main(request: Request):
    return templates.TemplateResponse(
        '01main.html',
        {
        "request": request,
        "items": mock_db_items
        }
        )


# --- 02item.html (상세 페이지) 라우트 ---
@app.get("/items/{item_id}", response_class=HTMLResponse)
async def read_item(request: Request, item_id: int):
    """
    '동적 경로'({item_id})를 사용하여 특정 아이템의 상세 페이지를 렌더링합니다.
    """
    
    # 3. Path Parameter로 받은 item_id를 사용해 DB에서 아이템 조회
    item = mock_db_items.get(item_id) 
    
    # 4. (중요) 아이템이 없는 경우 예외 처리
    if not item:
        # 간단하게 404 오류를 반환하거나, 오류 페이지를 렌더링할 수 있습니다.
        return templates.TemplateResponse("error.html", {"request": request, "item_id": item_id}, status_code=404)

    # 5. 조회된 'item' 데이터를 템플릿에 전달
    return templates.TemplateResponse("02item.html", {
        "request": request,
        "item_id": item_id, # URL에서 받은 ID
        "item": item        # DB에서 조회한 아이템 상세 정보
    })