from pathlib import Path

from pdf2image import convert_from_path

from models.documents_type import DocumentType


IMAGE_DIR = Path("converted_images")
async def detect_document_type(
    file_path: str
):
    suffix = Path(file_path).suffix.lower()

    if suffix == ".pdf":
        return DocumentType.PDF

    elif suffix == ".docx":
        return DocumentType.DOCX

    elif suffix == ".pptx":
        return DocumentType.PPTX

    elif suffix == ".txt":
        return DocumentType.TXT

    elif suffix in [".png", ".jpg", ".jpeg"]:
        return DocumentType.IMAGE

    return DocumentType.UNSUPPORTED

# async def convert_to_images(
#     file_path: str
# ):
#     document_type = await detect_document_type(file_path)

#     if document_type == DocumentType.PDF:
#         pass

#     elif document_type == DocumentType.IMAGE:
#         pass

#     elif document_type == DocumentType.DOCX:
#         pass

#     elif document_type == DocumentType.PPTX:
#         pass

#     else:
#         raise ValueError(
#             "Unsupported document type"
#         )

async def image_to_images(file_path: str):
    return [file_path]

async def convert_pdf_to_images(file_path: str):
    
    IMAGE_DIR.mkdir(
        exist_ok=True
    )

    pdf_path = Path(file_path)

    images = convert_from_path(pdf_path)

    image_paths = []

    for index, image in enumerate(images):

        output_path = (IMAGE_DIR / f"{pdf_path.stem}_page_{index+1}.png")

        image.save(output_path,"PNG")

        image_paths.append(str(output_path))

    return image_paths