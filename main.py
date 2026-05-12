from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello World"} 
  
@app.get("/status")
def get_status():
    return {
        "status": "online",
        "version": "0.1.0",
        "day": 1
    } 
@app.get("/about")
def get_about():
    return {
        "project": "My First API",
        "author": "Your Name",  # ← Change this!
        "course": "Applied Programming"
    }
@app.get("/square/{number}")
def calculate_square(number: int):
    result = number * number
    return {
        "number": number,
        "square": result,
        "calculation": f"{number} × {number} = {result}"
    }
@app.get("/student")
def get_student():
    return {
        "name": "Titi Rasouli",  
        "semester": 1,             
        "course": "Wirtschaftsinformatik",
        "university": "Hochschule Coburg"    
    }
@app.get("/double/{number}")
def calculate_double(number: int):
    result = number * 2
    return {
        "number": number,
        "double": result,
        "calculation": f"{number} × 2 = {result}"
    }