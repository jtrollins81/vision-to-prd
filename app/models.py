from pydantic import BaseModel

class PRDRequest(BaseModel):
    vision: str
    goals: str
    target_audience: str

class PRDResponse(BaseModel):
    content: str
