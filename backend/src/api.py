from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware

from .services.exceptions import FileFormatException
from .services.models import UploadResponse
from .services.services import DeepDive
from .settings.development import CORS_CONFIG

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=CORS_CONFIG["allow_origins"],
    allow_credentials=CORS_CONFIG["allow_credentials"],
    allow_methods=CORS_CONFIG["allow_methods"],
    allow_headers=CORS_CONFIG["allow_headers"],
)


@app.get("/healthcheck")
async def healthcheck():
    return {"status": "UP"}


@app.post("/process-audio/", response_model=UploadResponse)
async def create_upload_file(
    audio_file: UploadFile = File(..., description="Envie um arquivo .mp3 ou .wav")
):
    service = DeepDive()
    result = service.upload_audio(audio_file)

    if not result:
        raise FileFormatException()

    result = service.speech_to_text(result)

    return UploadResponse(**result)
