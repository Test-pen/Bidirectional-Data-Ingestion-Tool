from fastapi import APIRouter, File, UploadFile, HTTPException
from backend.db import get_clickhouse_client
import pandas as pd
import io

router = APIRouter()

@router.post("/")
async def upload_file(file: UploadFile = File(...)):
    if file.content_type not in ["text/csv", "text/tsv"]:
        raise HTTPException(status_code=400, detail="Only CSV/TSV files allowed")

    # Read file into DataFrame
    content = await file.read()
    sep = "\t" if file.filename.endswith(".tsv") else ","
    df = pd.read_csv(io.StringIO(content.decode()), sep=sep)

    client = get_clickhouse_client()
    table_name = "uploaded_data"  # or derive from filename
    try:
        client.command(f"DROP TABLE IF EXISTS {table_name}")
        columns = ", ".join(f"{col} String" for col in df.columns)
        client.command(f"CREATE TABLE {table_name} ({columns}) ENGINE = Memory")
        client.insert_df(table_name, df)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

    return {"message": f"{file.filename} uploaded successfully to {table_name}"}
