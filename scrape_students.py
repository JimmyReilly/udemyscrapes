import requests
import os
from bs4 import BeautifulSoup

username = 'luther@successwithluther.com'
password = ''

login_url = "https://www.udemy.com/join/login-popup/"
student_url = 'https://www.udemy.com/course/1023068/manage/students/?page='

pages = 88

header = {
	"Accept" : "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
	"Accept-Encoding" : "gzip, deflate, sdch, br",
	"Accept-Language" : "en-US,en;q=0.8,pt;q=0.6",
	"Cache-Control" : "max-age=0",
	"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36",
	"Referer" : login_url,
}

#get new session
session = requests.Session()

session.headers.update(header)

s = session.get(login_url)

soup = BeautifulSoup(s.text, 'html.parser')

csrftoken = ''

for tag in soup.find_all('input', {'name' : 'csrfmiddlewaretoken'}):
    csrftoken = tag.get('value');

#print(csrftoken)

params = {
	"email" : username,
	"password" : password,
	"locale" : 'en_US',
	'csrfmiddlewaretoken': csrftoken,
}

#log into udemy
s = session.post(login_url, params)

current_page = 1

while current_page <= pages:
    s = session.get(student_url + str(current_page))
    soup = BeautifulSoup(s.text, 'html.parser')
    
    for tag in soup.find_all('span', {'class' : 'fx'}):
        for a in tag.find_all('a'):
            print(a.get("href"))
    
    current_page += 1
