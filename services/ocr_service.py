import easyocr

reader= easyocr.Reader(['en'])

async def extract_text(image_path:str):

  result= reader.readtext(image_path, detail=0)

  return " ".join(result)

