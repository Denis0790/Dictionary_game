from fastapi import APIRouter, Depends
from bot_dictionary.backend.db.DBManager import DBManager

from bot_dictionary.backend.data.model_pydantic import DictionaryModel
from bot_dictionary.backend.db.dependency import get_db_service

insert_router = APIRouter(tags=["insert_words"])

add_word = DBManager()



@insert_router.post('/insert_words')
async def insert_words(words: DictionaryModel, db_manager: DBManager = Depends(get_db_service)):
    await db_manager.insert_word(words)
    return {'words': 'inserted'}
