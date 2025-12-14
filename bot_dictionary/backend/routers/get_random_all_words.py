from fastapi import APIRouter, Depends

from bot_dictionary.backend.db.DBManager import DBManager
from bot_dictionary.backend.db.dependency import get_db_service

get_all_router = APIRouter(tags=['get_all_words'])

@get_all_router.get('/get_all')
async def get_all_words(db_manager: DBManager = Depends(get_db_service)):
    ru_words = []
    result = await db_manager.get_random_all_words()
    for word in result:
        ru_words.append(word)
    return ru_words