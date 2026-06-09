from fastapi import UploadFile

UPLOAD_DIR = Path("uploaded_files")


async def save_file(
    file: UploadFile
):
    UPLOAD_DIR.mkdir(
        exist_ok=True
    )

    file_path = UPLOAD_DIR / file.filename

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
    saved_path= save_file(file)

    return {
      "File name": file.filename,
      "saved path":saved_path
    }