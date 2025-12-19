import uvicorn
from fastapi import FastAPI

from bot_dictionary.backend.routers.delete_word_router import delete_router
from bot_dictionary.backend.routers.get_random_all_words import get_all_router
from bot_dictionary.backend.routers.get_random_word_router import get_random_word_router
from bot_dictionary.backend.routers.insert_words_roter import insert_router

app = FastAPI()

app.include_router(insert_router)
app.include_router(get_all_router)
app.include_router(get_random_word_router)
app.include_router(delete_router)


@app.get("/")
async def root():
    return {"message": "I singing a song"}


if __name__ == "__main__":
    uvicorn.run("bot_dictionary.backend.main:app", host="127.0.0.1", port=8000, reload=True)