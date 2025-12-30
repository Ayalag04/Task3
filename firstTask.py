from fastapi import FastAPI
from fastapi.responses import JSONResponse
import json
import os

#run :  python -m uvicorn firstTask:app --reload
app = FastAPI()

FILE_PATH = "iris.json"

def read_data():
    if os.path.exists(FILE_PATH):
        with open(FILE_PATH, "r") as f:
            try:
                return json.load(f)
            except json.JSONDecodeError:
                return []  
    return []

def append_data(payload):
    data = read_data()
    data.append(payload)
    with open(FILE_PATH, "w") as f:
        json.dump(data, f, indent=2)  


@app.post("/add_payload")
def add_payload(payload: dict):  
    append_data(payload)  
    return JSONResponse(content={"message": "Payload added successfully"})  


@app.get("/last_10_payloads")
def get_last_10():
    data = read_data()  
    last_10 = data[-10:]  #last ten
    return JSONResponse(content=last_10)  
