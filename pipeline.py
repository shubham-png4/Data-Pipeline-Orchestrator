import time
import os
from dotenv import load_dotenv

# Load secret keys from .env
load_dotenv()
API_KEY = os.getenv("MY_API_KEY")

def retry(max_attempts=3, delay=2):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for i in range(max_attempts):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    print(f"Attempt {i+1} failed: {e}")
                    time.sleep(delay)
            raise Exception("Function failed after maximum retries.")
        return wrapper
    return decorator

@retry(max_attempts=3)
def process_data():
    print("Connecting to API...")
    if not API_KEY:
        raise ValueError("API Key missing!")
    print("Data processed successfully.")

if __name__ == "__main__":
    process_data()