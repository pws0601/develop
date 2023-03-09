from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from domain.answer import answer_router
from domain.question import question_router
from domain.user import user_router


#uvicorn main:app --reload
app = FastAPI()

origins = [
    "http://127.0.0.1:5173",
    "http://localhost:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

"""
@app.get("/hello")
def hello():
    return {"message":"안녕하세요 파이보"}
"""
# 라우터 등록
app.include_router(question_router.router)
app.include_router(answer_router.router)
app.include_router(user_router.router)
















##### 데이터 모델링 순서 #####
"""
import models
from database import engine
models.Base.metadata.create_all(bind=engine)

FastAPI 실행시 필요한 테이블들이 모두 생성됨
데이터베이스에 테이블이 존재하지 않을 경우에만 테이블을 생성하고
한번 생성된 테이블에 대한 변경 관리를 할수는 없음.

alembic을 사용하여 데이터베이스를 관리하는것이 효율 적이다.

1. alembic 초기화
alembic init migrations

alembic.ini 파일에서 db 접속정보 수정
(... 생략 ...)
sqlalchemy.url = sqlite:///./myapi.db
(... 생략 ...)

migrations/env.py 파일 수정
(... 생략 ...)
import models
(... 생략 ...)
# add your model's MetaData object here
# for 'autogenerate' support
# from myapp import mymodel
# target_metadata = mymodel.Base.metadata
target_metadata = models.Base.metadata
(... 생략 ...)


2. 리비전 파일 생성
alembic revision --autogenerate

3. 리비전 파일 실행
alembic upgrade head

4. User 테이블 생성 후

5. 리비전 파일 생성
alembic revision --autogenerate

6. 리비전 파일 실행
alembic upgrade head
"""
