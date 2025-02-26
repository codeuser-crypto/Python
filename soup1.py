import requests
from bs4 import BeautifulSoup
url = 'https://www.srmist.edu.in/'
response = requests.get(url)
if response.status_code == 200:
    with open('srm.html', 'w') as file:
        file.write(response.text)
    print('downloaded the Webpage')
    soup = BeautifulSoup(response.text, 'html.parser')
    print(soup)
else:
    print('Failed to download the Webpage. Error Code:', response.status_code)