import logging
import aiohttp

BASE_URL = "http://127.0.0.1:8000"
ENDPOINT = "/insert_words"

async def add_words_in_backend(en_word: str, ru_word: str):
    url = f"{BASE_URL}{ENDPOINT}"

    payload = {
        "word_en": en_word,
        "word_ru": ru_word
    }

    try:
        async with aiohttp.ClientSession() as session:
            async with session.post(url, json=payload, timeout=5) as response:
                result_data = await response.json()
                if response.status in [200, 201]:
                    return result_data
    except aiohttp.ClientConnectorError:
        logging.critical(f"Не удалось подключиться к FastAPI по адресу {BASE_URL}. Проверьте, запущен ли uvicorn.")
        return False
    except Exception:
        return False

