import requests
import os
import sys
from bs4 import BeautifulSoup

header = {
	"Accept" : "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
	"Accept-Encoding" : "gzip, deflate, sdch, br",
	"Accept-Language" : "en-US,en;q=0.8,pt;q=0.6",
	"Cache-Control" : "max-age=0",
	"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36",
	"Referer" : 'http://google.com',
}

user_url = "https://www.udemy.com"

url_get_params = "?key=subscribed_courses&subscribed_courses="

session = requests.Session()

session.headers.update(header)

for line in sys.stdin:
    line = line.rstrip().strip()
    request_url = user_url + line + url_get_params
    
    next_page = True
    page = 1
    first_result = '63erhf43yhthgyukuyff'
    first_recorded = False
    
    print("*Start*")
    print(line)
    
    while next_page:
        s = session.get(request_url + str(page))
        soup = BeautifulSoup(s.text, 'html.parser')
        
        next_page = False
        
        if not (first_result in str(soup.html)):
            print("+++++++PAGE: " + str(page))
            
            for tag in soup.find_all('div', {'id' : 'learning'}):
                for li in tag.find_all('li', {'class' : 'card'}):
                    for anchor in li.find_all('a'):
                        print(anchor.get("href"))
                        if (not first_recorded) and (page == 1):
                            first_result = anchor.get("href")
                            first_recorded = True
                            print(">>>>>>>" + first_result)
            
            for tag in soup.find_all('ul', {'class' : 'pagination'}):
                for li in tag.find_all('li'):
                    for a in tag.find_all('a'):
                        if 'Next' in a.text:
                            next_page = True

        if next_page:
            page += 1
        else:
            print("*END*")
            
