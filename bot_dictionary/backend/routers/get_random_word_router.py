from fastapi import APIRouter, Depends

from bot_dictionary.backend.db.DBManager import DBManager
from bot_dictionary.backend.db.dependency import get_db_service

get_random_word_router = APIRouter(tags=['get_random_word'])

@get_random_word_router.get('/get_random')
async def get_random_word(db_manager: DBManager = Depends(get_db_service)):
    result = await db_manager.get_random_all_words()
    return result[0]