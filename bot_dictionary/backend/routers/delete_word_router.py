from fastapi import APIRouter, Depends
from bot_dictionary.backend.db.DBManager import DBManager
from bot_dictionary.backend.db.dependency import get_db_service


delete_router = APIRouter(tags=["delete_words"])

@delete_router.delete("/delete")
async def delete_word(word_en: str, db: DBManager = Depends(get_db_service)):
    print(word_en)
    if await db.delete_word_in_db(word_en):
        return "Успешно удалено!"
    else:
        return "Что то пошло не так!"