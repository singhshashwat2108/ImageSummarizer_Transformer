from fastapi import APIRouter, UploadFile, File
from services.document_service import process_document

router = APIRouter(
    prefix="/documents",
    tags=["Documents"]
)


@router.post("/upload")
async def upload_document(
    file: UploadFile = File(...)):
    return await process_document(file)