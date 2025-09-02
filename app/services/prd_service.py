from app.models import PRDRequest
import os

# Optional: pip install openai
try:
    import openai
    OPENAI_AVAILABLE = True
except ImportError:
    OPENAI_AVAILABLE = False

# Load API key from environment variable
OPENAI_API_KEY = os.getenv("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")

# Prompt template for PRD generation
PRD_PROMPT_TEMPLATE = """
You are a product manager. Generate a detailed Product Requirements Document (PRD)
based on the following input:

Vision:
{vision}

Goals:
{goals}

Target Audience:
{target_audience}

Structure the PRD with clear headings:
- Vision
- Goals
- Target Audience
- Core Features
- Nice-to-have Features
- Success Metrics
- Risks / Dependencies
"""

def generate_prd(request: PRDRequest) -> str:
    """
    Generate a PRD using OpenAI API if available, otherwise return a stub.
    """
    prompt = PRD_PROMPT_TEMPLATE.format(
        vision=request.vision,
        goals=request.goals,
        target_audience=request.target_audience
    )

    # If OpenAI not installed or API key missing, return stub
    if not OPENAI_AVAILABLE or not OPENAI_API_KEY:
        return f"""
        # Product Requirements Document (Stub)

        ## Vision
        {request.vision}

        ## Goals
        {request.goals}

        ## Target Audience
        {request.target_audience}

        ---
        (AI not configured. Set OPENAI_API_KEY and install openai to generate real PRDs.)
        """

    # Call OpenAI GPT model
    response = openai.ChatCompletion.create(
        model="gpt-4",
        api_key=OPENAI_API_KEY,
        messages=[
            {"role": "system", "content": "You are a senior product manager."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.7,
        max_tokens=1000
    )

    prd_text = response.choices[0].message.content
    return prd_text
