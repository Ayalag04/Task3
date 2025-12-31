import json
import os
import typer
from typing import Optional
#the format to run:python exe2.py add '{\"name\": \"Iris\", \"age\": 25}'

app = typer.Typer()

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

    if not isinstance(data, list):
        raise ValueError("Invalid data format: expected a list from read_data")

    data.append(payload)

    with open(FILE_PATH, "w") as f:
        json.dump(data, f, indent=2)


@app.command()
def add(payload: str):
    try:
        # המר את המידע שהתקבל ל-JSON
        data = json.loads(payload)
        append_data(data)
        typer.echo("Payload added successfully!")
    except json.JSONDecodeError:
        typer.echo("Error: Invalid JSON format")

@app.command("get_last_10")
def get_last_10():
    data = read_data()
    last_10 = data[-10:]  
    if last_10:
        for item in last_10:
            print(item)
    else:
        typer.echo("No data found")

if __name__ == "__main__":
    app()
