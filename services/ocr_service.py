import easyocr

reader= easyocr.Reader(['en'], model_storage_directory=r"D:\Deep_learning\Text_Summarizer\Model_cache")

def extract_text(image_path:str):

  result= reader.readtext(image_path, detail=0)

  return " ".join(result)


def extract_text_from_images(image_paths: list[str]):

    pages = []

    for image_path in image_paths:

        text = extract_text(
            image_path
        )

        pages.append(text)

    return "\n".join(pages)