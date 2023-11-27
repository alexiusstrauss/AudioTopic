from uuid import uuid4

import speech_recognition as sr
from fastapi import UploadFile
from pydub import AudioSegment as Asegment

from .exceptions import RecognizeException


class DeepDive:
    """
    Service responsavel por upload, conversao e validação do audio
    """

    def upload_audio(self, file: UploadFile):
        """
        Function upload audio mp3 or wav
        """
        file_extension = file.filename.split(".")[-1]
        if file_extension not in ["mp3", "wav"]:
            return False

        file_id = str(uuid4())
        file_location = f"audio_files/{file_id}.{file_extension}"

        with open(file_location, "wb+") as file_object:
            file_object.write(file.file.read())

        return {"file_id": file_id, "file_location": file_location}

    def speech_to_text(self, upload_audio: dict) -> dict:
        """
        Function convert audio to text
        """
        recognizer = sr.Recognizer()
        audio_file_path = upload_audio["file_location"]
        audio_file_path = self.__convert_mp3_to_wav(audio_file_path)

        with sr.AudioFile(audio_file_path) as source:
            audio_data = recognizer.record(source)
            try:
                text = recognizer.recognize_google(
                    audio_data=audio_data, language="pt-BR"
                )
                upload_audio["original_context"] = text
            except (sr.UnknownValueError, sr.RequestError) as exc:
                raise RecognizeException() from exc

        return upload_audio

    def __convert_mp3_to_wav(self, mp3_file_path):
        wav_file_path = mp3_file_path.replace(".mp3", ".wav")
        try:
            Asegment.from_mp3(mp3_file_path).export(wav_file_path, format="wav")
        except Exception as exc:
            raise RecognizeException() from exc
        return wav_file_path
