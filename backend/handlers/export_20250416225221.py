from fastapi import APIRouter, HTTPException, Query
from fastapi.responses import StreamingResponse
from backend.db import get_clickhouse_client
import pandas as pd
import io

router = APIRouter()

@router.get("/")
def export_query(query: str = Query(..., description="SELECT query to export")):
    client = get_clickhouse_client()
    try:
        df = client.query_df(query)
        stream = io.StringIO()
        df.to_csv(stream, index=False)
        stream.seek(0)
        return StreamingResponse(stream, media_type="text/csv", headers={
            "Content-Disposition": "attachment; filename=export.csv"
        })
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
