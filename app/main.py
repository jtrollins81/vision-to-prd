from fastapi import FastAPI

app = FastAPI(
    title="Vision → PRD Generator",
    description="Turns plain-language ideas into structured Product Requirements Documents",
    version="0.1.0"
)

@app.get("/")
def root():
    return {"message": "Vision → PRD Generator API is live"}
