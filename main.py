from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def home():
    return {"message": "Hello from Praveen Kumar Reddy!"}


@app.get("/users")
def users():
    return {
        "users": ["Praveen", "Rahul", "Arjun"]
    }