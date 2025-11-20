import sqlite3

def create_db():
    conn = sqlite3.connect("url.db")
    c = conn.cursor()
    c.execute("""CREATE TABLE IF NOT EXISTS urls (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    long_url TEXT NOT NULL,
                    short_code TEXT NOT NULL UNIQUE,
                    clicks INTEGER DEFAULT 0
                )""")
    conn.commit()
    conn.close()

def insert_url(long_url, short_code):
    conn = sqlite3.connect("url.db")
    c = conn.cursor()
    c.execute("INSERT INTO urls (long_url, short_code) VALUES (?, ?)", (long_url, short_code))
    conn.commit()
    conn.close()

def get_url(short_code):
    conn = sqlite3.connect("url.db")
    c = conn.cursor()
    c.execute("SELECT long_url, clicks FROM urls WHERE short_code = ?", (short_code,))
    result = c.fetchone()

    if result:
        long_url, clicks = result
        c.execute("UPDATE urls SET clicks = clicks + 1 WHERE short_code = ?", (short_code,))
        conn.commit()
        conn.close()
        return long_url
    conn.close()
    return None
