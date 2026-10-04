from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def home():
    return {"message": "Hello from Render!"}


@app.get("/users")
def users():
    return {
        "users": ["Praveen", "Rahul", "Arjun"]
    }