from fastapi import APIRouter, Depends

from bot_dictionary.backend.db.DBManager import DBManager
from bot_dictionary.backend.db.dependency import get_db_service

check_router = APIRouter(tags=['check_answer'])

@check_router.post('/check{word_en}')
async def get_all_words(word_en: str, db_manager: DBManager = Depends(get_db_service)):
    result = await db_manager.check_word(word_en)
    return {'result': result}