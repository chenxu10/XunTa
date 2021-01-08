from bs4 import BeautifulSoup
import requests
import urllib.request
import re
from collections import Counter
import webbrowser


def search_query():
    page = 1
    url = "http://www.google.com/search?q=xushen" + "&start=" + str((page - 1) * 10)
    webbrowser.open_new_tab(url)

if __name__ == "__main__":
    search_query()
