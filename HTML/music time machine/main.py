from typing import TextIO
from spotipy.oauth2 import SpotifyOAuth
import spotipy

ID = '21310a4720cf4f658cda97fcacc21412'
SECRET = '6b8d2b78afe344508c8a81f61169cdeb'
sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope='playlist-modify-private',
        redirect_uri='http://example.com',
        client_id=ID,
        client_secret=SECRET,
        show_dialog=True,
        cache_path='token.txt',
        username='K'
    )
)
user_id = sp.current_user()['id']

from bs4 import BeautifulSoup
import requests

year = int(input('Which year do you want to travel to? Type the date in this format: YYYY\n'))
response = requests.get(f"https://www.billboard.com/charts/year-end/{year}/hot-100-songs/")
web_site = response.text
soup = BeautifulSoup(web_site, 'html.parser')
data = soup.find_all(name='div', class_='o-chart-results-list-row-container')
for i in data:
    try:
        with open(f"songs_of_{year}_year.txt", 'a', encoding='utf-8') as create:
            create.write(
                f"{i.find(name='h3', id='title-of-a-story').getText().strip()}\n")
    except FileNotFoundError:
        with open(f"songs_of_{year}_year.txt", 'wr', encoding='utf-8') as create:
            create.write(
                f"{i.find(name='h3', id='title-of-a-story').getText().strip()}\n")

uri = []
with open(f"songs_of_{year}_year.txt") as data_songs:
    songs = [data_songs.readlines()]

for song in songs:
    data_search = sp.search(q=f"track:{song[:len(song) - 2:]} year:{year}", type='track')
    print(data_search)
    try:
        res = data_search['tracks']['items'][0]['uri']
        uri.append(res)
    except IndexError:
        print(f"{song} it doesnt exist in spotify. Skiped")
