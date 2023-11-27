import os

from fastapi import FastAPI, File, Request, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse

from .services.exceptions import FileFormatException, NotFoundException
from .services.models import UploadResponse
from .services.services import DeepDive
from .settings.development import CORS_CONFIG, OPEN_AI_TOKEN
from .summarization.engines import LangChain

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
async def create_upload_file(request: Request, audio_file: UploadFile = File(..., description="arquivo .mp3 ou .wav")):
    lang_chain = LangChain(api_key=OPEN_AI_TOKEN)
    service = DeepDive(llm_engine=lang_chain)
    service.validate_api_token()
    response = service.upload_audio(audio_file)

    if not response:
        raise FileFormatException()

    response = service.speech_to_text(response)
    response = service.summarize_text(response=response)
    response = service.create_audio_from_summary(response=response)
    response = service.create_link_to_summary(request=request, response=response)

    return UploadResponse(**response)


@app.get("/download/{file_id}")
async def download_file(file_id: str):
    file_path = f"audio_files/{file_id}_audio_summarize.mp3"

    if not os.path.exists(file_path):
        raise NotFoundException()

    return FileResponse(file_path, media_type='audio/mpeg', filename=f"{file_id}_audio_summarize.mp3")
