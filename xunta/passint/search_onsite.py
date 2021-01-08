import webbrowser
import requests
import sys
import bs4
import random

def find_referral(pos="data science",time="2020",company="wayfair"):
    pos = '"' + pos + '"'
    time = '"' + time + '"'
    company = '"' + company + '"'
    s = pos + " " + time + " " + company
    s = s + ' site:1point3acres.com'
    url = "https://www.google.com/search?q={}".format(s)
    webbrowser.open_new_tab(url)

if __name__ == "__main__":
    find_referral("data science","2020","wayfair")