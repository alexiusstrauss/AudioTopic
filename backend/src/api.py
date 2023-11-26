from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware

from .exceptions import FileFormatException
from .models import UploadResponse
from .services import DeepDive

app = FastAPI()

# Configuração do middleware CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
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
