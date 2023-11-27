from unittest.mock import MagicMock, patch

from src.services.services import DeepDive
from src.summarization.engines import LangChain
from src.summarization.interfaces import Summarization


class MockSummarization(Summarization):
    def summarize(self, text: str) -> str:
        return "Mocked Summary"


def test_summarize_text_success():
    llm_engine = MockSummarization()
    deepdive = DeepDive(llm_engine=llm_engine)
    response = {"original_context": "Original text"}

    result = deepdive.summarize_text(response)

    assert "summary_context" in result
    assert result["summary_context"] == "Mocked Summary"


@patch.object(LangChain, "token_is_valid")
def test_validate_api_token_with_langchain(mock_token_is_valid):
    llm_engine = LangChain(api_key="fake-api-key")
    deepdive = DeepDive(llm_engine=llm_engine)

    deepdive.validate_api_token()

    mock_token_is_valid.assert_called_once()


def test_validate_api_token_with_non_langchain():
    llm_engine = MagicMock()  # Criar um mock que não é LangChain
    deepdive = DeepDive(llm_engine=llm_engine)

    deepdive.validate_api_token()

    # Certificar-se de que token_is_valid não é chamado, pois llm_engine não é LangChain
    llm_engine.token_is_valid.assert_not_called()
