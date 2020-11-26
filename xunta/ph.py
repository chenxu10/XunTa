import webbrowser
import requests
import sys
import bs4

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


