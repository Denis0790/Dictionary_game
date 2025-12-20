import logging
import aiohttp

BASE_URL = "http://127.0.0.1:8000"
ENDPOINT = "/delete"

async def delete_word_api(en_word: str):
    url = f"{BASE_URL}{ENDPOINT}"
    params = {"word_en": en_word}

    try:
        async with aiohttp.ClientSession() as session:
            async with session.delete(url, params=params, timeout=5) as response:
                result_data = await response.json()
                if response.status in [200, 201]:
                    return result_data
    except aiohttp.ClientConnectorError:
        logging.critical(f"Не удалось подключиться к FastAPI по адресу {BASE_URL}. Проверьте, запущен ли uvicorn.")
        return False
    except Exception:
        return False