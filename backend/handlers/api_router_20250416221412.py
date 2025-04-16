from fastapi import APIRouter
from pydantic import BaseModel
from clickhouse_driver import Client

router = APIRouter()

# Define the expected request body
class ConnectRequest(BaseModel):
    host: str
    port: int
    username: str
    password: str
    database: str

@router.post("/connect")
def connect_clickhouse(credentials: ConnectRequest):
    try:
        client = Client(
            host=credentials.host,
            port=credentials.port,
            user=credentials.username,
            password=credentials.password,
            database=credentials.database,
        )
        version = client.server_version
        return {"message": "Connected successfully 🎉", "version": version}
    except Exception as e:
        return {"error": str(e)}
