from http import HTTPStatus
from io import BytesIO
from unittest.mock import patch

from fastapi import UploadFile
from fastapi.testclient import TestClient

from src.api import app

client = TestClient(app)

# ... [outros testes]


@patch("src.services.services.DeepDive.upload_audio")
@patch("src.services.services.DeepDive.speech_to_text")
@patch("src.services.services.DeepDive.summarize_text")
@patch("src.services.services.DeepDive.create_audio_from_summary")
@patch("src.services.services.DeepDive.create_link_to_summary")
def test_create_upload_file(
    mock_upload_audio,
    mock_speech_to_text,
    mock_summarize_text,
    mock_create_audio_from_summary,
    mock_create_link_to_summary,
):
    fake_audio_file = BytesIO(b"Fake audio content")

    # Configurar os mocks
    mock_upload_audio.return_value = {
        "file_id": "5d08289f-6a1d-4984-94c7-228cfeccd506",
        "file_location": "audio_files/test_audio.wav",
    }
    mock_speech_to_text.return_value = {
        "file_id": "5d08289f-6a1d-4984-94c7-228cfeccd506",
        "original_context": "Contexto do audio enviado",
    }
    mock_summarize_text.return_value = {
        "file_id": "5d08289f-6a1d-4984-94c7-228cfeccd506",
        "summary_context": "Resumo do audio",
    }
    mock_create_audio_from_summary.return_value = {
        "file_id": "5d08289f-6a1d-4984-94c7-228cfeccd506",
        "mp3_summary_url": "audio_files/test_audio_summarized.mp3",
    }
    mock_create_link_to_summary.return_value = {
        "file_id": "5d08289f-6a1d-4984-94c7-228cfeccd506",
        "summary_url": "http://localhost:8000/download/5d08289f-6a1d-4984-94c7-228cfeccd506",
    }

    # Criar um cliente de teste e realizar a requisição
    client = TestClient(app)
    response = client.post(
        "/process-audio/",
        files={"audio_file": ("test.mp3", fake_audio_file, "audio/mp3")},
    )

    assert response.status_code == HTTPStatus.OK
