from bs4 import BeautifulSoup
import requests
import random

response = requests.get("https://www.timeout.com/newyork/movies/best-movies-of-all-time")

timeout_webpage = response.text

soup = BeautifulSoup(timeout_webpage, "html.parser")

top_100_movies = soup.find_all(name="h3", class_="_h3_cuogz_1")

movie_titles = [(" ".join(movie.getText().split("\xa0")).split("(")[0]) for movie in top_100_movies]

movie_titles.pop()

with open("movies.txt", "w") as file:
    for movie in movie_titles:
        file.write(f"{movie}\n")

print(movie_titles[random.randint(1, 100)].split(". ")[1])
