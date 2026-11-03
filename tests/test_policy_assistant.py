from unittest.mock import MagicMock, patch
from policy_assistant import ask_claude
import pytest
from anthropic import APIConnectionError

def test_successful_response():
    mock_response = MagicMock()
    mock_response.content = [
        MagicMock(type="text", text="Student is eligible.")
    ]

    with patch("policy_assistant.client.messages.create") as mock_create:
        mock_create.return_value = mock_response

        result = ask_claude("Am I eligible?")

        assert result["answer"].strip() == "Student is eligible."
        mock_create.assert_called_once()

def test_unsuccessful_response():
    with pytest.raises(ValueError):
        ask_claude("")

def test_api_error_response():
    with patch("policy_assistant.client.messages.create") as mock_create:
        mock_create.side_effect = APIConnectionError(request=MagicMock())

        with pytest.raises(APIConnectionError):
            ask_claude("Am I eligible?")