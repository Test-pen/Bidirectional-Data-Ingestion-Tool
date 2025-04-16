from fastapi import FastAPI
from handlers.api_router import router as api_router

app = FastAPI()

app.include_router(api_router)

@app.get("/")
def root():
    return {"message": "Backend is up and running 🚀"}
