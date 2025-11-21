import sys
import os
from dotenv import load_dotenv

# Add src directory to path
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'src'))

from src.config import validate_config
from src.models import get_model
from src.utils import measure_latency

def verify_models():
    print("Loading environment...")
    load_dotenv()
    
    try:
        validate_config()
        print("Configuration valid.")
        
        creds_path = os.getenv("GOOGLE_APPLICATION_CREDENTIALS")
        if creds_path:
            print(f"Found credentials file: {creds_path}")
        else:
            print("No GOOGLE_APPLICATION_CREDENTIALS found in environment.")
            
    except ValueError as e:
        print(f"Configuration error: {e}")
        # Continue anyway to see if we can initialize models if creds are present but not env vars
    
    models_to_test = [
        ("vertexai", "gemini-2.5-flash"),
        ("vertexai", "gemini-2.5-flash-lite")
    ]
    
    for provider, model_name in models_to_test:
        print(f"\nTesting {provider}/{model_name}...")
        try:
            model = get_model(provider, model_name)
            print(f"Model initialized: {model}")
            
            print("Sending test message...")
            response, latency = measure_latency(model.invoke, "Hello, are you working?")
            
            print(f"Response received in {latency:.2f}s")
            print(f"Content: {response.content}")
            print("SUCCESS")
            
        except Exception as e:
            print(f"FAILED: {e}")

if __name__ == "__main__":
    verify_models()
