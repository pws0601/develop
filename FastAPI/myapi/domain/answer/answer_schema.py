from pydantic import BaseModel, validator
import datetime

class AnswerCreate(BaseModel):
    content:str

    #AnswerCreate 스키마에 content값이 저장될때 실행.
    #공백을 허용하지 않는다.
    @validator('content')
    def not_empty(cls, v):
        if not v or not v.strip():
            raise ValueError('빈 값은 허용되지 않습니다.')
        return v

class Answer(BaseModel):
    id: int
    content: str
    create_date: datetime.datetime

    class Config:
        orm_mode = True