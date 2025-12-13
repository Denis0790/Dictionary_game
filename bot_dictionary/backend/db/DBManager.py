import aiosqlite
import asyncio
from bot_dictionary.backend.data.model_pydantic import DictionaryModel


class DBManager:
    def __init__(self, db_name = 'database.db'):

        self.db_name = db_name
        self.cursor = None
        self.conn = None

    async def connect(self):
        self.conn = await aiosqlite.connect(self.db_name)
        self.cursor = await self.conn.cursor()
        await self.create_table()
        await self.conn.commit()


    async def create_table(self):
        await self.cursor.execute('''CREATE TABLE IF NOT EXISTS Words (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        word_en TEXT NOT NULL UNIQUE,
        word_ru TEXT NOT NULL UNIQUE
        )
         ''')

    async def insert_word(self, words: DictionaryModel):
        add_word = 'INSERT INTO Words (word_en, word_ru) VALUES (?, ?)'
        values = (words.word_en, words.word_ru)
        await self.cursor.execute(add_word, values)
        await self.conn.commit()

    async def get_random_all_words(self):
        await self.cursor.execute("SELECT * FROM Words ORDER BY RANDOM()")
        all_words = await self.cursor.fetchall()
        return all_words

    async def check_word(self, word_ru):
        pass

    async def close(self):
        if self.conn:
            await self.conn.close()