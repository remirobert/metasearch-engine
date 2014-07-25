import time
import manage_database
from search import search
from search_news import searchNews
from search_images import search_image
from search_video import search_video
from search_torrent import search_torrent

def update_result_search(conn, keyword):
    search_results = search(keyword)
    image_search = search_image(keyword)
    news_results = searchNews(keyword)
    videos_search = search_video(keyword)
    torrent_search = search_torrent(keyword)
    manage_database.fill_new_entry(conn, keyword, search_results, image_search, \
                                   news_results, videos_search, torrent_search)

def update_word_search(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM keyword ORDER BY nb DESC")
    for i in cursor.fetchall():
        print "update : ", i[1]
        update_result_search(conn, i[1])

def run_robot():
    conn = manage_database.connect_database()
    while True:
        update_word_search(conn)
        time.sleep(1)
