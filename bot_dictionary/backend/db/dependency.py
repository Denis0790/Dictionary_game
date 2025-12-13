from bot_dictionary.backend.db.DBManager import DBManager


async def get_db_service():
    db_service = DBManager(db_name='database.db')
    await db_service.connect()
    try:
        yield db_service
    finally:
        await db_service.close()