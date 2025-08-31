from app.models import PRDRequest

def generate_prd(request: PRDRequest) -> str:
    """
    Placeholder PRD generator.
    Later this will call AI, but for now it just formats input.
    """
    return f"""
    # Product Requirements Document

    ## Vision
    {request.vision}

    ## Goals
    {request.goals}

    ## Target Audience
    {request.target_audience}

    ---
    (This is a placeholder PRD. AI generation coming soon!)
    """
