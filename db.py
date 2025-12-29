import aiosqlite

DB_NAME = "appeals.db"

async def init_db():
    async with aiosqlite.connect(DB_NAME) as db:
        await db.execute("""
        CREATE TABLE IF NOT EXISTS appeals (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER,
            full_name TEXT,
            subject TEXT,
            workplace TEXT,
            phone TEXT,
            text TEXT,
            status TEXT
        )
        """)
        await db.commit()


async def save_appeal(data, user_id):
    async with aiosqlite.connect(DB_NAME) as db:
        cursor = await db.execute("""
        INSERT INTO appeals (user_id, full_name, subject, workplace, phone, text, status)
        VALUES (?, ?, ?, ?, ?, ?, ?)
        """, (
            user_id,
            data["full_name"],
            data["subject"],
            data["workplace"],
            data["phone"],
            data["text"],
            "Yangi"
        ))
        await db.commit()
        return cursor.lastrowid


async def get_appeal(appeal_id):
    async with aiosqlite.connect(DB_NAME) as db:
        cursor = await db.execute(
            "SELECT * FROM appeals WHERE id = ?", (appeal_id,)
        )
        return await cursor.fetchone()
