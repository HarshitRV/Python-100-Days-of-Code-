import requests
from bs4 import BeautifulSoup

response = requests.get("https://www.empireonline.com/movies/features/best-movies-2/")

soup = BeautifulSoup(response.text, "html.parser")
movie_list = soup.find_all(name="h3")

# list_100 = [movie.get_text() for movie in movie_list]
print(movie_list)