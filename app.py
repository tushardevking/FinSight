from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

app=FastAPI()

class AskRequest(BaseModel):
    question: str
    company: str
    year: Optional[int]

@app.post("/ask")
async def query(queryask: AskRequest) :
    return {"question": queryask.question,
            "company": queryask.company}

@app.get("/metrics")   
def metrics():
    return{"Latency": "0s"} 
           
@app.get("/health")  
def health():
    return{"status": "OK"}  

