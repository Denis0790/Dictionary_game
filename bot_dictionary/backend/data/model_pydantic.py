from pydantic import BaseModel

class DictionaryModel(BaseModel):
    word_en: str
    word_ru: str