import requests
import webbrowser
from bs4 import BeautifulSoup

url = 'https://www.srmist.edu.in/'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
print(soup.prettify())
print(soup.title)
webbrowser.open(url)
webbrowser.open_new(url)
webbrowser.open_new_tab(url)