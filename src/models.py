"""Model factory and abstraction for different providers."""
from typing import Optional, List
from langchain_openai import ChatOpenAI
from langchain_google_vertexai import ChatVertexAI
from langchain_core.language_models import BaseChatModel

def get_model(
    provider: str,
    model_name: str,
    temperature: float = 0.7,
    tags: Optional[List[str]] = None,
    **kwargs
) -> BaseChatModel:
    """
    Factory function to get a chat model from a supported provider.
    
    Args:
        provider: The model provider ('openai' or 'vertexai')
        model_name: The specific model name (e.g., 'gpt-4', 'gemini-2.5-flash')
        temperature: Sampling temperature
        tags: List of tags for LangSmith tracing
        **kwargs: Additional provider-specific arguments
        
    Returns:
        BaseChatModel: Configured chat model instance
    """
    tags = tags or []
    
    if provider.lower() == "openai":
        return ChatOpenAI(
            model=model_name,
            temperature=temperature,
            tags=tags,
            **kwargs
        )
    
    elif provider.lower() == "vertexai":
        # Vertex AI specific configuration can be added here if needed
        return ChatVertexAI(
            model_name=model_name,
            temperature=temperature,
            tags=tags,
            **kwargs
        )
    
    else:
        raise ValueError(f"Unsupported provider: {provider}. Supported providers: openai, vertexai")
