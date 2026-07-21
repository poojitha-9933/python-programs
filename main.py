from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {
        "name": "Poojitha",
        "internship_title": "Python Intern"
    }