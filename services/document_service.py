from fastapi import UploadFile
from services.converter_service import detect_document_type, image_to_images, convert_pdf_to_images
import uuid

UPLOAD_DIR = Path("uploaded_files")


async def save_file(
    file: UploadFile
):
    UPLOAD_DIR.mkdir(
        exist_ok=True
    )

    unique_name = f"{uuid.uuid4()}_{file.filename}"
    file_path = UPLOAD_DIR / unique_name

    content = await file.read()

    with open(file_path, "wb") as f:
        f.write(content)

    return str(file_path)

async def process_document(
    file: UploadFile):

    allowed_types = [
        "application/pdf",
        "image/png",
        "image/jpeg"
    ]

    if file.content_type not in allowed_types:
        return {
            "error": "Unsupported file type"
        }
    saved_path= await save_file(file)

    document_type = await detect_document_type(saved_path)

    if document_type == DocumentType.PDF:
      return await convert_pdf_to_images(file_path)

    elif document_type == DocumentType.IMAGE:
        return await image_to_images(file_path)

    return {
        "filename":file.filename,
        "file_type": document_type
    }