from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from contextlib import asynccontextmanager

import firebase_admin
from firebase_admin import credentials, firestore, db

from config import settings
from schema.item import itemInfo

@asynccontextmanager
async def lifespan(app : FastAPI):
    try:
        cred_path = settings.FIREBASE_SERVICE_ACCOUNT_PATH
        cred = credentials.Certificate(cred_path)

        firebase_admin.initialize_app(
            credential=cred,
            options={'databaseURL': settings.FIREBASE_DATABASE_URL}
            )
        print('Firebase Admin SDK 초기화')
    except ValueError as e:
        print(f'실패 : {e}')
    except FileNotFoundError:
        print(f'키 오류 경로: {cred_path}')
    yield

app = FastAPI(title='antioch', version='0.1.0', lifespan=lifespan) # docs_url, redoc_url 보안을 위해 추후 비활성화

templates = Jinja2Templates(directory='templates')

@app.get('/', response_class=HTMLResponse)
async def read_main(request: Request):
    try:
        fs_client = firestore.client()
        fs_itemInfo = fs_client.collection('item').stream()
        rt_itemStatus = db.reference(path='itemStatus')

        items = []
        for doc in fs_itemInfo:
            doc_data = doc.to_dict()
            if not doc_data:
                continue

            doc_data['id'] = doc.id
            try:
                item_obj = itemInfo.model_validate(doc_data)
                items.append(item_obj)
            except Exception as e:
                print(f'파싱 오류 {doc.id} : {e}')

        return templates.TemplateResponse(
            '01main.html',
            {
            'request': request,
            'items':items
            }
            )
    except Exception as e:
        print(f"메인 페이지 로드 오류: {e}")
        return templates.TemplateResponse(
            '99error.html', 
            {'request': request, 'error': str(e)}, 
            status_code=500
        )
"""
@app.get("/items/{item_id}", response_class=HTMLResponse)
async def read_item(request: Request, item_id: int):
    item = mock_db_items.get(item_id)

    if not item:
        return templates.TemplateResponse(
            '99error.html',
            {
                'request': request,
                'item_id': item_id
            },
            status_code=404
            )

    return templates.TemplateResponse("02item.html", {
        "request": request,
        "item_id": item_id, # URL에서 받은 ID
        "item": item        # DB에서 조회한 아이템 상세 정보
    })
"""