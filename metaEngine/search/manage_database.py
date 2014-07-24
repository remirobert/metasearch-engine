import sqlite3
import os
import manage_database_search

def create_database():
    conn = sqlite3.connect("database.sql")
    cursor = conn.cursor()

    print "creation table"
    cursor.execute('''CREATE TABLE keyword (id INTEGER PRIMARY KEY AUTOINCREMENT, word TEXT)''')

    cursor.execute('''CREATE TABLE search (id INTEGER PRIMARY KEY AUTOINCREMENT,
    id_word INTEGER, url TEXT, title TEXT, content TEXT)''')

    cursor.execute('''CREATE TABLE images (id INTEGER PRIMARY KEY AUTOINCREMENT,
    id_word INTEGER, url TEXT, img_src TEXT)''')

    cursor.execute('''CREATE TABLE news (id INTEGER PRIMARY KEY AUTOINCREMENT,
    id_word INTEGER, url TEXT, title TEXT, content TEXT, date TEXT)''')

    cursor.execute('''CREATE TABLE videos (id INTEGER PRIMARY KEY AUTOINCREMENT,
    id_word INTEGER, url TEXT, title TEXT, content TEXT)''')

    cursor.execute('''CREATE TABLE torrent (id INTEGER PRIMARY KEY AUTOINCREMENT,
    id_word INTEGER, url TEXT, title TEXT, link TEXT, seed TEXT, leech TEXT)''')

    conn.commit()
    conn.close()

def fill_new_entry(conn, request, search_results, 
                   image_search, news_search, videos_search, torrent_search):
    cursor = conn.cursor()

    arg = (request,)
    cursor.execute('''INSERT INTO keyword (word) VALUES(?)''', arg)
    word_id = cursor.lastrowid;
    conn.commit()
    for i in search_results:
        arg = (word_id, i["url"], i["title"], i["content"],)
        cursor.execute('''INSERT INTO search (id_word, url, title, content) 
        VALUES(?, ?, ?, ?)''', arg)        
        conn.commit()

    for i in image_search:
        arg = (word_id, i["url"], i["img_src"])
        cursor.execute('''INSERT INTO images (id_word, url, img_src) 
        VALUES(?, ?, ?)''', arg)        
        conn.commit()

    for i in news_search:
        arg = (word_id, i["url"], i["title"], i["content"], i["date"],)
        cursor.execute('''INSERT INTO news (id_word, url, title, content, date) 
        VALUES(?, ?, ?, ?, ?)''', arg)        
        conn.commit()

    for i in videos_search:
        arg = (word_id, i["url"], i["title"], i["content"])
        cursor.execute('''INSERT INTO videos (id_word, url, title, content) 
        VALUES(?, ?, ?, ?)''', arg)        
        conn.commit()

    for i in torrent_search:
        arg = (word_id, i["url"], i["title"], i["magnetlink"], i["seed"], i["leech"],)
        cursor.execute('''INSERT INTO torrent (id_word, url, title, link, seed, leech) 
        VALUES(?, ?, ?, ?, ?, ?)''', arg)
        conn.commit()

def search_word(conn, request, type_search):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM keyword WHERE word=?", (request,))
    response_database = cursor.fetchone()
    if response_database == None:
        return None
    print "find result database : ", response_database
    print "id response : ", response_database[0]
    
    if type_search == "search":
        return manage_database_search.database_search_search(cursor, response_database[0])
    elif type_search == "images":
        return manage_database_search.database_images_search(cursor, response_database[0])
    elif type_search == "news":
        return manage_database_search.database_news_search(cursor, response_database[0])
    elif type_search == "videos":
        return manage_database_search.database_videos_search(cursor, response_database[0])
    elif type_search == "torrent":
        return manage_database_search.database_torrent_search(cursor, response_database[0])
    return None

def connect_database():
    db = os.path.exists("database.sql")
    if db == False:
        create_database()
    try:
        conn = sqlite3.connect("database.sql")
    except:
        create_database()
    print "connection success database : ", conn
    return conn
