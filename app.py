from fastapi import FastAPI
from pydantic import BaseModel
from openai_function import openai_function_response

app = FastAPI()

class Email(BaseModel):
    from_email: str
    content: str

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post("/")
def analyse_email(email: Email):
    content = email.content
    result = openai_function_response(content)
    return result
    
    