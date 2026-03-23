# telegram_database.py

# import library
import psycopg2
import os
from dotenv import load_dotenv

# load const from .env file
load_dotenv()

# create connect with DB
DATABASE = os.environ.get("DATABASE")
USERNAME = os.environ.get("USER_NAME")
PASSWORD = os.environ.get("PASSWORD")
conn = psycopg2.connect(database=DATABASE, user=USERNAME, password=PASSWORD)

# create all tables for bot
def create_database():
    print('create a tables')
    query = """
        CREATE TABLE IF NOT EXISTS users (
            id SERIAL PRIMARY KEY,
            telegram_id BIGINT UNIQUE NOT NULL
        );

        CREATE TABLE IF NOT EXISTS default_words (
            id SERIAL PRIMARY KEY,
            word VARCHAR(255) UNIQUE NOT NULL,
            translation VARCHAR(255) NOT NULL
        );
        
        CREATE TABLE IF NOT EXISTS words (
            id SERIAL PRIMARY KEY,
            word VARCHAR(255) UNIQUE NOT NULL,
            translation VARCHAR(255) NOT NULL
        );

        CREATE TABLE IF NOT EXISTS user_words (
            id SERIAL PRIMARY KEY,
            user_id INTEGER NOT NULL,
            word_id INTEGER NOT NULL,
            FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE,
            FOREIGN KEY (word_id) REFERENCES words(id) ON DELETE CASCADE,
            UNIQUE (user_id, word_id)
        );
    """
    with conn.cursor() as cur:
        cur.execute(query)

# find user id by telegram user id
def get_user_id(user_id):
    print('find user')
    query = "SELECT id FROM users WHERE telegram_id = %s;"
    with conn.cursor() as cur:
            cur.execute(query, (user_id, ))
            result = cur.fetchall()
            print(result)
            if result:
                return result[0][0]
            else:
                print('add user to database')
                query = "INSERT INTO users (telegram_id) VALUES (%s);"
                cur.execute(query, (user_id, ))
                conn.commit()

                query = "SELECT id FROM users WHERE telegram_id = %s;"
                cur.execute(query, (user_id, ))
                result = cur.fetchall()
                print(result)
                if result:
                    return result[0][0]
                else:
                    return None

# find all words for user
def get_words(user_id):
    query = """
        SELECT w.id, w.word, w.translation
        FROM words w
        LEFT JOIN user_words uw ON w.id = uw.word_id AND uw.user_id = %s
        WHERE uw.user_id = %s
        UNION ALL
        SELECT  w.id, w.word, w.translation
        FROM default_words w
    """
    with conn.cursor() as cur:
        cur.execute(query, (user_id, user_id))
        result = cur.fetchall()
        if result:
            return result
        else:
            return None

# find user words for delete
def get_words_for_delete(user_id):
    query = """
        SELECT w.id, w.word, w.translation
        FROM words w
        LEFT JOIN user_words uw ON w.id = uw.word_id AND uw.user_id = %s
        WHERE uw.user_id = %s
    """
    with conn.cursor() as cur:
        cur.execute(query, (user_id, user_id))
        result = cur.fetchall()
        if result:
            return result
        else:
            return None

# add word to database for user
def add_word(user_id, word, transl):
    with conn.cursor() as cur:
        print('add word to database')
        query = """INSERT INTO words (word, translation) VALUES (%s, %s) RETURNING id;
        """
        cur.execute(query, (word, transl))
        conn.commit()
        result = cur.fetchall()
        word_id = result[0][0]
        print(result)

        print('add word to user')
        query = """INSERT INTO user_words (user_id, word_id) VALUES (%s, %s);
        """
        cur.execute(query, (user_id, word_id))
        conn.commit()

# delete word for user
# 1 delete from user_words
# 2 delete from words
def delete_word(user_id, word_id):
    with conn.cursor() as cur:
        print('delete word from database - user-words')
        query = """DELETE FROM user_words WHERE user_id = %s AND word_id = %s;
        """
        cur.execute(query, (user_id, word_id))
        conn.commit()

        print('delete word from words')
        query = """DELETE FROM words WHERE id = %s;
        """
        cur.execute(query, (word_id, ))
        conn.commit()

# load words for all users
def load_default_words():
    default_words = [
            ("red", "красный"),
            ("blue", "синий"),
            ("green", "зеленый"),
            ("yellow", "желтый"),
            ("black", "черный"),
            ("white", "белый"),
            ("purple", "фиолетовый"),
            ("orange", "оранжевый"),
            ("brown", "коричневый"),
            ("gray", "серый"),
            ("I", "я"),
            ("you", "ты"),
            ("he", "он"),
            ("she", "она"),
            ("it", "оно"),
            ("we", "мы")]
    with conn.cursor() as cur:
        print(f'check default word')
        query = """SELECT COUNT(id) FROM default_words;
        """
        cur.execute(query)
        result = cur.fetchall()
        if not result[0][0]:
            for w in default_words:
                with conn.cursor() as cur:
                    print(f'add default word {w} to database')
                    query = """INSERT INTO default_words (word, translation) VALUES (%s, %s);
                    """
                    cur.execute(query, (w[0], w[1]))
                    conn.commit()

# start
if conn:
    print('Database is connected')
    create_database()
    load_default_words()

