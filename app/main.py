from fastapi import FastAPI
from app.api import prd

app = FastAPI(title="Vision-to-PRD API")

# Include PRD-related endpoints
app.include_router(prd.router, prefix="/prd", tags=["prd"])
