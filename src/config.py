"""Configuration management for the evaluation project."""
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# LangSmith Configuration
LANGCHAIN_API_KEY = os.getenv("LANGCHAIN_API_KEY")
LANGCHAIN_TRACING_V2 = os.getenv("LANGCHAIN_TRACING_V2", "true")
LANGCHAIN_PROJECT = os.getenv("LANGCHAIN_PROJECT", "model-version-eval")

# OpenAI Configuration
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

def validate_config():
    """Validate that required environment variables are set."""
    missing = []
    
    if not LANGCHAIN_API_KEY:
        missing.append("LANGCHAIN_API_KEY")
    if not OPENAI_API_KEY:
        missing.append("OPENAI_API_KEY")
    
    if missing:
        raise ValueError(
            f"Missing required environment variables: {', '.join(missing)}\n"
            "Please copy .env.example to .env and fill in your API keys."
        )
    
    return True
