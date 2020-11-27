import webbrowser
import requests
import sys
import bs4
import random

def format_loc(loc):
    if loc == "newyork":
        loc = "new york"
    loc =  '"' + loc + '"'
    return loc
    
def make_search_urls(loc, companies):
    loc = format_loc(loc)
    urls = []
    search_terms = ['"hiring" ("head of" OR "director" or "manager")' + 
    ' "data science" site:linkedin.com', 
    '"recruiter" "data scientist" site:linkedin.com']
    
    for c in companies:
        for s in search_terms:
            newc = '"' + c + '"'
            query = loc + ' ' + newc + ' ' + s
            url = "https://www.google.com/search?q={}".format(query)
            urls.append(url)
    return urls


if __name__ == "__main__":
    urls = make_search_urls(sys.argv[1:][0], sys.argv[2:])
    for u in urls:
        webbrowser.open_new_tab(u)
        print('start openining all recruiter and data scientist...')
        res = requests.get(u)
        if res.status_code == 200:
            soup = bs4.BeautifulSoup(res.text, 'html.parser')
            linklist = [link for link in soup.find_all('a')]
            openlist = []
            for link in linklist:
                if "q=https://www.linkedin.com/in" in link.get('href'):
                    hyperlink = link.get('href').partition('=')[2]
                    hyperlink = hyperlink.partition('&')[0]
                    openlist.append(hyperlink)   
        else:
            print('request failed')

        for i in openlist:   
            webbrowser.open_new_tab(i)