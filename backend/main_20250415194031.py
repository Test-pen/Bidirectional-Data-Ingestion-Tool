main.py

from fastapi import FastAPI

app = FastAPI()

@app.get("/") def read_root(): return {"message": "Backend is up and running 🚀"}

Then in terminal, run:

uvicorn main:app --reload