import webbrowser
import requests
import sys
import bs4

def make_search_urls(companies):
    urls = []
    search_terms = ['"hiring" ("head of" OR "director" or "manager")' + 
    ' "data science" "boston" site:linkedin.com', 
    '"recruiter" "data scientist" "boston" site:linkedin.com']
    
    for c in companies:
        for s in search_terms:
            newc = '"' + c + '"'
            query = newc + ' ' + s
            url = "https://www.google.com/search?q={}".format(query)
            urls.append(url)
    return urls


if __name__ == "__main__":
    urls = make_search_urls(sys.argv[1:])
    for u in urls:
        webbrowser.open_new_tab(u)


search_terms = ['"hiring" ("head of" OR "director" or "manager") "data science" "boston" site:linkedin.com',
'"recruiter" "data scientist" "boston" site:linkedin.com']

# s = '"' + sys.argv[1:][0] + '"'
# for term in search_terms:
#     url = "https://www.google.com/search?q={}".format(s + ' ' + term)
#     webbrowser.open_new_tab(url)





