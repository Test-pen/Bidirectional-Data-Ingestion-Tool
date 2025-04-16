# backend/schema.py

from pydantic import BaseModel
from typing import List, Optional

class ClickHouseConnectionParams(BaseModel):
    host: str
    port: int
    database: str
    user: str
    jwt_token: str

class FileUploadMetadata(BaseModel):
    delimiter: Optional[str] = ","
    filename: Optional[str] = None

class TableColumnSelection(BaseModel):
    table_name: str
    selected_columns: List[str]

class IngestionRequest(BaseModel):
    source: str  # "clickhouse" or "flatfile"
    target: str  # "clickhouse" or "flatfile"
    connection: Optional[ClickHouseConnectionParams] = None
    file_metadata: Optional[FileUploadMetadata] = None
    column_selection: Optional[TableColumnSelection] = None
