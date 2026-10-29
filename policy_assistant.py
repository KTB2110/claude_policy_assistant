from anthropic import Anthropic, NotFoundError, APIError, RateLimitError
from dotenv import load_dotenv
import time

load_dotenv()

client = Anthropic()

def ask_claude(question: str) -> dict:

    if not question.strip():
        raise ValueError("Empty Question String")
    

    start = time.perf_counter()

    try:
        answer = client.messages.create(
            model="claude-haiku-4-5",
            system="You are a university admissions expert. You answer in short and sweet answers and explain it in ASD-STE100 format.",
            max_tokens=500,
            messages=[
                {
                    "role": "user",
                    "content": question
                }
            ]
        )

        end = time.perf_counter()

        answer_text = ""
        for block in answer.content:
            if block.type == "text":
                answer_text += block.text + "\n"

        return {
            "answer": answer_text,
            "model": answer.model,
            "input_tokens": answer.usage.input_tokens,
            "output_tokens": answer.usage.output_tokens,
            "stop_reason": answer.stop_reason,
            "latency_seconds": (end - start)
        }

    except NotFoundError:
        print("Model Not Found")
        raise
    except RateLimitError:
        print("Rate Limit Exceeded")
        raise
    except APIError:
        print("Anthropic API Error")
        raise
    finally:
        end = time.perf_counter()
        print(f"API Latency: {end - start} seconds")
    

if __name__ == "__main__":


    # ask_claude("What is a merit scholarship?")
    ask_claude("   ")