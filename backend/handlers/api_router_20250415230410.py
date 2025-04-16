from fastapi import APIRouter
from services.db import get_clickhouse_client

router = APIRouter()

@router.post("/connect")
def connect_clickhouse():
    try:
        client = get_clickhouse_client()
        version = client.server_version
        return {"message": "Connected successfully 🎉", "version": version}
    except Exception as e:
        return {"error": str(e)}
