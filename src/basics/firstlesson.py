from fastapi import FastAPI, Header
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

@app.get('/')
async def read_root():
    return {"message": "Hello World!"}

# To pass a parameter in the api
"""
@app.get('/greet/{name}')
async def greet_name(name: str) -> dict:
    return {"message": f"Hello {name}"}
"""

# To pass the name as query parameter -> /greet/?name=mohith
"""
@app.get('/greet')
async def greet_query(name: str) -> dict:
    return {"message": f"Hello {name}"}
"""

# To have both path parameter and query parameter
@app.get('/greet/{name}')
async def greet_both(name: str, age: int) -> dict:
    return {"message": f"Hello {name}", "age": age}

# To make parameters optional
@app.get('/greet')
async def greet_optional(name: Optional[str] = "mohith", age: int = 0) -> dict:
    return {"message": f"Hello {name}", "age": age}

# Schema for Book
class BookCreateModel(BaseModel):
    title  : str
    author : str

@app.post('/create_book')
async def create_book(book_data: BookCreateModel):
    return {
        "title" : book_data.title,
        "author": book_data.author
    }

@app.get('/get_headers', status_code=200)
async def get_headers(accept: str = Header(None), content_type: str = Header(None), user_agent: str = Header(None), host: str = Header(None)):
    request_headers = {}
    request_headers["Accept"] = accept
    request_headers["Content-Type"] = content_type
    request_headers["User-Agent"] = user_agent
    request_headers["Host"] = host
    return request_headers
