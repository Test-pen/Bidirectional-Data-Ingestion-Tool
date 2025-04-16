from fastapi import APIRouter

router = APIRouter()

@router.post("/connect")
def connect():
    return {"status": "connect endpoint working"}

@router.get("/tables")
def get_tables():
    return {"tables": []}

@router.post("/columns")
def get_columns():
    return {"columns": []}

@router.post("/preview")
def preview_data():
    return {"preview": []}

@router.post("/ingest")
def ingest_data():
    return {"status": "ingestion started"}

@router.get("/status")
def get_status():
    return {"status": "idle"}
