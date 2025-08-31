from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class VisionInput(BaseModel):
    vision: str

@app.post("/generate_prd")
def generate_prd(input_data: VisionInput):
    """
    Placeholder endpoint.
    Takes a 'vision' string and returns a dummy PRD response.
    """
    return {
        "vision": input_data.vision,
        "prd": "Project Requirements Document (placeholder)",
    }

