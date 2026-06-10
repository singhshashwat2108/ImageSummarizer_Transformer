from enum import Enum

class DocumentType(str, Enum):
    PDF = "pdf"
    IMAGE = "image"
    DOCX = "docx"
    PPTX = "pptx"
    TXT = "txt"
    UNSUPPORTED = "unsupported"