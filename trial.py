from pdf2image import convert_from_path
from services.ocr_service import extract_text

# images = convert_from_path(
#     "uploaded_files/sample.pdf"
# )

# image[0].save("converted_image/page1.png","PNG")

print(extract_text("converted_image/page1.png"))

