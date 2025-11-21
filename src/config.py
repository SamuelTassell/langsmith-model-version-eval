"""Configuration management for the evaluation project."""
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# LangSmith Configuration
LANGSMITH_API_KEY = os.getenv("LANGSMITH_API_KEY")
LANGSMITH_TRACING_V2 = os.getenv("LANGSMITH_TRACING_V2", "true")
LANGSMITH_PROJECT = os.getenv("LANGSMITH_PROJECT", "model-version-eval")

# OpenAI Configuration
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Google Vertex AI Configuration
GOOGLE_APPLICATION_CREDENTIALS = os.getenv("GOOGLE_APPLICATION_CREDENTIALS")

def validate_config():
    """Validate that required environment variables are set."""
    missing = []
    
    if not LANGSMITH_API_KEY:
        missing.append("LANGSMITH_API_KEY")
    
    # Check for OpenAI key if being used (warning only if missing, as user might only use Vertex)
    if not OPENAI_API_KEY and not GOOGLE_APPLICATION_CREDENTIALS:
        missing.append("OPENAI_API_KEY or GOOGLE_APPLICATION_CREDENTIALS")

    if missing:
        raise ValueError(
            f"Missing required environment variables: {', '.join(missing)}\n"
            "Please copy .env.example to .env and fill in your API keys."
        )
    
    return True
