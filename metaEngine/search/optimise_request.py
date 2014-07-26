import sys
sys.path.append("search/")
sys.path.append("engine/")
sys.path.append("search/engine/")
from search import search
from search_news import searchNews
from search_images import search_image
from search_video import search_video
from search_torrent import search_torrent
import manage_database

def download(keyword, word_id):
    conn = manage_database.connect_database()
    search_results = search(keyword)
    image_search = search_image(keyword)
    news_results = searchNews(keyword)
    videos_search = search_video(keyword)
    torrent_search = search_torrent(keyword)
    manage_database.fill_new_entry(conn, keyword, search_results, image_search, \
                                   news_results, videos_search, torrent_search, word_id)
    conn.close()

