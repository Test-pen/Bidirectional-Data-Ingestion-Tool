from fastapi import APIRouter
from handlers.db import connect_clickhouse
from handlers.export import export_data
from handlers.upload import upload_data

from schemas.connect_schema import ConnectRequest  # assuming you created this schema

router = APIRouter()

@router.post("/connect", summary="Connect Clickhouse", description="Connects to a ClickHouse database")
def connect(payload: ConnectRequest):
    return connect_clickhouse(payload)

# Add other endpoints similarly
