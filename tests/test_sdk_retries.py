import httpx2
from anthropic import Anthropic, DefaultHttpxClient, RateLimitError
from dotenv import load_dotenv
import pytest

load_dotenv() 

def test_sdk_retries():
    attempts = 0

    def fake_server(request):
        nonlocal attempts
        attempts += 1

        print(f"HTTP Attempt: {attempts}")

        return httpx2.Response(
            status_code=429,
            json={
                "error": {
                    "type" : "rate_limit_error",
                    "message" : "Rate Limit Exceeded"
                }
            }
        )

    transport = httpx2.MockTransport(fake_server)

    with Anthropic(max_retries=2,
                   http_client=DefaultHttpxClient(transport=transport)) as client:
        
        with pytest.raises(RateLimitError):
            client.messages.create(
                model="claude-haiku-4-5",
                max_tokens=500,
                messages=[
                    {"role": "user", "content": "Hello"}
                ]
            )

        assert attempts == 3

