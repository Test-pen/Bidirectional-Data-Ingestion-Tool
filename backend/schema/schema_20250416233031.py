# backend/schema/schema.py

from pydantic import BaseModel
from typing import Optional
from datetime import datetime

# Used for incoming data from flat files
class FlatFileRow(BaseModel):
    id: int
    name: str
    email: str
    signup_date: Optional[datetime] = None
    purchase_amount: Optional[float] = None

# Used for transformed data before sending to ClickHouse
class ClickHouseRow(BaseModel):
    id: int
    name: str
    email: str
    signup_date: Optional[str]  # ClickHouse might expect a string timestamp
    purchase_amount: Optional[float]
    file_source: Optional[str]  # e.g. "users_2023.csv"
