from http.client import responses


# from binstar_client import STATUS_CODES  # 상태코드
from fastapi import FastAPI, HTTPException  # Fastapi 임포드  -> http에 대한 비동기 방식을 처리하는 서버
from pydantic import BaseModel # 데이터 유효성 검사와 설정 관리에 사용되는 라이브러리(모델링 쉽고 강력함)
from starlette.middleware.base import BaseHTTPMiddleware, RequestResponseEndpoint

# 요청과 응답사이에 특정 작업 수행


# 미들웨어는 모든 요청에 대해 실행되며, 요청을 처리하기 전에 응답을 반환하기 전에 특징 작업을 수행할 수 있음
# 예를 들아 로깅, 인증, cors처리, 압축들...

import logging

from starlette.requests import Request  # 요청에 대한 내용
from starlette.responses import Response  # 응답에 대한 내용

app = FastAPI(
    title= "My API",             # 앱의 제목
    description= "This is a sample API",   # 앱의 주석(설명)
    version= "1.0.0",                       # 앱의 버전
    docs_url = None
)  # 객체를 생성하고 app 변수에 넣음

@app.get("/")   # http://localhost/ 의 라우트(경로)
async def read_root():  
    return {"Hello": "World"}

# 서버실행 -> cd .\AI_Python\  ->  uvicorn main:app --reload --port 8001
# 크롬 -> 주소 : http://localhost:8001/
# 크롬 -> 주소 : http://127.0.0.1:8001/




class LoggingMiddleware(BaseHTTPMiddleware):  # 로그를 콘솔에 출력하는 용도
    logging.basicConfig(level=logging.INFO)  # 로그 출력 추가

    async def dispatch(self, request, call_next):
        logging.info(f"Req: {request.method} {request.url}")
        responses = await call_next(request)
        logging.info(f"Status Code: {responses.status_code}")
        return responses
app.add_middleware(LoggingMiddleware)


class Item(BaseModel):  # 아이템 객제 생성(BaseModel : 객체 연결 -> 상속)
    name :str                    # 상품명 : 문자열
    description : str = None      # 상품설명 : 무자열
    price : float
    tax : float = None


@app.get("item/{item_id}")
async def read_item(item_id: int, q:str = None):
    return {"item_id" : item_id, "q": q}
# item_id : 상품의 번호 -> 경로 매개변수
# q : 쿼리 매개변수 (기본값 none)


@app.post("/items/")
async def create_item(item: Item):  # BaseModel 은 데이터 모델링 쉽게 도와주고 유효성검사도 수행
    # 잘못된 데이터가 들어오면 422 오류코드를 반환
    return item
