# from bs4 import BeautifulSoup
# import requests

# response = requests.get("https://news.ycombinator.com/")

# soup = BeautifulSoup(response.text, "html.parser")

# # print(soup.prettify())

# titles = soup.select(".storylink")
# scores = soup.select(".score")

# title_list = [title.get_text() for title in titles]
# link_list = [title.get("href") for title in titles]
# score_list = [int(score.get_text().strip(" points")) for score in scores]

# # print(title_list)
# # print("\n\n")
# # print(link_list)
# # print("\n\n")
# # print(score_list)

# highest_upvote = max(score_list)
# index = score_list.index(highest_upvote)

# print(f"TITLE: {title_list[index]}\nLINK: {link_list[index]}\nUPVOTE: {highest_upvote}")

import requests
from bs4 import BeautifulSoup

URL = "https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(URL)
website_html = response.text

soup = BeautifulSoup(website_html, "html.parser")

all_movies = soup.find_all(name="h3", class_="title")

movie_titles = [movie.getText() for movie in all_movies]
movies = movie_titles[::-1]

with open("movies.txt", mode="w") as file:
    for movie in movies:
        file.write(f"{movie}\n")