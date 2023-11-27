from pydantic import BaseModel


class UploadResponse(BaseModel):
    file_id: str
    original_context: str = None
    summary_context: str = None
    summary_url: str = None
