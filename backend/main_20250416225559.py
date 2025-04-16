from fastapi import FastAPI
from handlers.api_router import router as api_router  # make sure this is the right path

app = FastAPI(
    title="Bidirectional Data Ingestion",
    description="API to handle ClickHouse connections, data upload, and export operations.",
    version="1.0.0"
)

app.include_router(api_router)

@app.get("/")
def root():
    return {"message": "Backend is up and running 🚀"}
