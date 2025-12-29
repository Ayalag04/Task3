from fastapi import FastAPI
from fastapi.responses import JSONResponse
import json
import os

app = FastAPI()

# נתיב הקובץ (שמור את הנתיב ל-iris.json או כל שם אחר שצריך)
FILE_PATH = "iris.json"

# פונקציה לעיון בנתונים קיימים
def read_data():
    if os.path.exists(FILE_PATH):
        with open(FILE_PATH, "r") as f:
            try:
                return json.load(f)
            except json.JSONDecodeError:
                return []  # אם יש בעיה בקריאת הנתונים, נחזיר רשימה ריקה
    return []

# פונקציה להוספת Payload חדש
def append_data(payload):
    data = read_data()
    data.append(payload)
    with open(FILE_PATH, "w") as f:
        json.dump(data, f, indent=2)  # הוספתי 'indent=2' כדי להדפיס את הנתונים בצורה קריאה

# פונקציה להוספת payload
@app.post("/add_payload")
def add_payload(payload: dict):  # מקבל את ה-payload בצורה ישירה כ-dict
    append_data(payload)  # מוסיף את ה-payload לקובץ
    return JSONResponse(content={"message": "Payload added successfully"})  # הודעה למשתמש

# פונקציה להחזרת 10 ה-payloads האחרונים
@app.get("/last_10_payloads")
def get_last_10():
    data = read_data()  # קורא את כל הנתונים
    last_10 = data[-10:]  # לוקח את 10 האחרונים
    return JSONResponse(content=last_10)  # מחזיר את ה-10 האחרונים
