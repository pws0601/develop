from pydantic import BaseModel
from fastapi import Form
from typing import List, Optional

class Item(BaseModel):
    item: str
    status: str

class Todo(BaseModel):
    id: Optional[int]
    item: str

    @classmethod
    def as_form(
        cls,
        item: str = Form(...)
    ):
        return cls(item=item)
        
        

    class Config:
        schema_extra = {
            "example" : {
                "id" : 1,
                "item" : "Example Schema!"
            }
        }

class TodoItem(BaseModel):    
    item: str
    class Config:
        schema_extra = {
            "example" : {                
                "item" : "Read the next chapter of the book"
            }
        }

class TodoItems(BaseModel):
    todos: List[TodoItem]

    class Config:
        shema_extra = {
            "example" : {
                "todos" : [
                    {
                        "item" : "Example schema 1!"
                    },
                    {
                        "item" : "Example schema 2!"
                    }
                ]
            }
        }