from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from starlette import status

from database import get_db
from domain.question import question_schema, question_crud
from domain.user.user_router import get_current_user
from models import User

from typing import List

router = APIRouter(
    prefix="/api/question",
)

# with 문과 함께 쓰는 방법
"""
@router.get("/list")
def question_list():    
    with get_db() as db:
        _question_list = db.query(Question).order_by(Question.create_date.desc()).all()
    
    return _question_list
"""

# Depends 사용
@router.get("/list", response_model=question_schema.QuestionList)
def question_list(db: Session = Depends(get_db), page: int = 0, size: int = 10):
    total, _question_list = question_crud.get_question_list(db, skip=page*size, limit=size)
    return {'total': total, 'question_list':_question_list}

@router.get("/detail/{question_id}", response_model=question_schema.Question)
def question_detail(question_id: int,db: Session = Depends(get_db)):
    question = question_crud.get_question(db,question_id=question_id)
    return question

@router.post("/create", status_code=status.HTTP_204_NO_CONTENT)
def question_create(
    _question_create: question_schema.QuestionCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
    ):
    question_crud.create_question(db=db, question_create=_question_create, user=current_user)