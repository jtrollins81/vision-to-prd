from pydantic import BaseModel
from typing import List, Optional

class VisionInput(BaseModel):
    problem: str
    target_users: str
    success_criteria: Optional[str] = None
    core_features: List[str] = []
    nice_to_have_features: List[str] = []
    constraints: Optional[str] = None
    assumptions: Optional[str] = None

class PRDOutput(BaseModel):
    prd: str
