from fastapi import APIRouter, UploadFile, File, HTTPException
import pandas as pd, io
from app.core.dfg import dataframe_to_event_log, discover_dfg, get_variants
from app.core.performance import analyze_performance

router = APIRouter()

@router.post("/dfg")
async def dfg(file: UploadFile = File(...)):
    try:
        content = await file.read()
        df = pd.read_csv(io.BytesIO(content))
        log = dataframe_to_event_log(df)
        return discover_dfg(log)
    except Exception as e:
        raise HTTPException(400, str(e))

@router.post("/variants")
async def variants(file: UploadFile = File(...)):
    content = await file.read()
    df = pd.read_csv(io.BytesIO(content))
    log = dataframe_to_event_log(df)
    return get_variants(log)

@router.post("/performance")
async def performance(file: UploadFile = File(...)):
    content = await file.read()
    df = pd.read_csv(io.BytesIO(content))
    log = dataframe_to_event_log(df)
    return analyze_performance(log)
