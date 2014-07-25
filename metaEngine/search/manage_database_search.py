import sqlite3

def database_torrent_search(cursor, id_search):
    cursor.execute("SELECT * FROM torrent WHERE id_word=?", (id_search,))
    data_search = []
    for i in cursor.fetchall():
        current_dict = {}
        current_dict["url"] = i[2]
        current_dict["title"] = i[3]
        current_dict["link"] = i[4]
        current_dict["seed"] = i[5]
        current_dict["leech"] = i[6]
        data_search.append(current_dict)
    return data_search

def database_videos_search(cursor, id_search):
    cursor.execute("SELECT * FROM videos WHERE id_word=?", (id_search,))
    data_search = []
    for i in cursor.fetchall():
        current_dict = {}
        current_dict["url"] = i[2]
        current_dict["title"] = i[3]
        current_dict["content"] = i[4]
        data_search.append(current_dict)
    return data_search

def database_news_search(cursor, id_search):
    cursor.execute("SELECT * FROM news WHERE id_word=?", (id_search,))
    data_search = []
    for i in cursor.fetchall():
        current_dict = {}
        current_dict["url"] = i[2]
        current_dict["title"] = i[3]
        current_dict["content"] = i[4]
        current_dict["date"] = i[5]
        data_search.append(current_dict)
    return data_search

def database_images_search(cursor, id_search):
    cursor.execute("SELECT * FROM images WHERE id_word=?", (id_search,))
    data_search = []
    for i in cursor.fetchall():
        current_dict = {}
        current_dict["url"] = i[2]
        current_dict["img_src"] = i[3]
        data_search.append(current_dict)
    return data_search

def database_search_search(cursor, id_search):    
    cursor.execute("SELECT * FROM search WHERE id_word=?", (id_search,))
    data_search = []
    for i in cursor.fetchall():
        current_dict = {}
        current_dict["url"] = i[2]
        current_dict["title"] = i[3]
        current_dict["content"] = i[4]
        data_search.append(current_dict)
    return data_search
