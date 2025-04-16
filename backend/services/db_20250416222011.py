from fastapi import APIRouter
from pydantic import BaseModel
from clickhouse_connect import get_client

router = APIRouter()

class ClickHouseConnectionRequest(BaseModel):
    host: str
    port: int
    username: str
    password: str
    database: str
    secure: bool = False  # optional; default False

@router.post("/connect")
def connect_clickhouse(conn: ClickHouseConnectionRequest):
    try:
        client = get_client(
            host=conn.host,
            port=conn.port,
            username=conn.username,
            password=conn.password,
            database=conn.database,
            secure=conn.secure
        )
        version = client.server_version
        return {"message": "Connected successfully 🎉", "version": version}
    except Exception as e:
        return {"error": str(e)}
