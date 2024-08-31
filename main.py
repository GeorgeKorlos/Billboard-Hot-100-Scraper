import requests
from bs4 import BeautifulSoup


choice = input("Which year do you want to travel to? Type the date is this format YYYY-MM-DD: ")

URL = f'https://www.billboard.com/charts/hot-100/{choice}'

response = requests.get(URL)
page = response.text

soup = BeautifulSoup(page, 'html.parser')
songs = soup.select('li ul li h3')
song_list = [song.getText().strip() for song in songs]

with open('songs.txt', 'w') as file:
    for song in song_list:
        file.write(f"{song}\n")