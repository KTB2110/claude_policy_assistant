from unittest.mock import MagicMock, patch
from policy_assistant import ask_claude
import pytest
from anthropic import APIConnectionError, RateLimitError

class APIResponse:
    content = []
    model = ""
    usage = []
    stop_reason = ""

def test_successful_response():
    mock_response = MagicMock(spec=APIResponse)
    mock_response.content = [
        MagicMock(type="text", text="Student is eligible.")
    ]
    mock_response.usage = MagicMock(input_tokens=100, output_tokens=1000)

    with patch("policy_assistant.client.messages.create") as mock_create:
        mock_create.return_value = mock_response

        result = ask_claude("Am I eligible?")

        assert result["answer"].strip() == "Student is eligible."
        assert result["input_tokens"] == 100
        assert result["output_tokens"] == 1000
        mock_create.assert_called_once()

def test_unsuccessful_response():
    with pytest.raises(ValueError):
        ask_claude("")

def test_api_error_response():
    with patch("policy_assistant.client.messages.create") as mock_create:
        mock_create.side_effect = APIConnectionError(request=MagicMock())

        with pytest.raises(APIConnectionError):
            ask_claude("Am I eligible")

def test_rate_limit_error_response():
    with patch("policy_assistant.client.messages.create") as mock_create:
        mock_create.side_effect = RateLimitError(message=MagicMock(), response=MagicMock(), body=MagicMock())

        with pytest.raises(RateLimitError):
            ask_claude("Am I eligible")