import requests
from bs4 import BeautifulSoup
url= "https://www.imdb.com/chart/top/"
response= requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
if response.status_code == 200:
    soup= BeautifulSoup(response.text, "html.parser")
    movies=soup.select(".ipc-title__text")[:10]
    print("top 10 movies:")
    for idx, movie in enumerate(movies, start=1):
        print(f"{idx}. {movie.text}")
else:
    print(f"Failed to download the webpage. Error code: {response.status_code}")