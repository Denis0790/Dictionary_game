import logging
import aiohttp

BASE_URL = "http://127.0.0.1:8000"
ENDPOINT = "/get_random"

async def get_random_word_in_db():
    url = f"{BASE_URL}{ENDPOINT}"
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url, timeout=5) as response:
                result_data = await response.json()
                if response.status in [200, 201]:
                    return result_data
                print(f" vot on {result_data}")
    except aiohttp.ClientConnectorError:
        logging.critical(f"Не удалось подключиться к FastAPI по адресу {BASE_URL}. Проверьте, запущен ли uvicorn.")
        return False
    except Exception:
        return False