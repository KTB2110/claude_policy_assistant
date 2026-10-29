from dotenv import load_dotenv
from anthropic import Anthropic, NotFoundError, RateLimitError, APIError
import time

load_dotenv()

client = Anthropic()

start = time.perf_counter()
try: 
    msg = client.messages.create(
        model = "claude-sonnet-5-53248234",
        max_tokens = 500,
        system = "You are a university admissions expert and answer in short and sweet language about any questions of this domain",
        messages = [{
            "role" : "user",
            "content" : "What is a scholarship"
        }]
    )
    
    print(msg)
except NotFoundError:
    print("This claude model was not found. Please try again with a valid model name!")
except RateLimitError:
    print("Rate Limit Exceeded: Please wait for more capacity!")
except APIError as e:
    print(f"API Error: {e}")
finally:
    end = time.perf_counter()
    print(f"API request latency: {end - start} seconds")

