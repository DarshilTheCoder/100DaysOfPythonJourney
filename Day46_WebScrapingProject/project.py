from bs4 import BeautifulSoup
import requests
import spotipy
import os
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv

load_dotenv()
client_id = os.getenv('Client_ID')
client_secret_key = os.getenv('Client_Secret')
redirect_URI = os.getenv('Redirect_URI')
user_answer = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD = ")
sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://example.com",
        client_id=client_id,
        client_secret=client_secret_key,
        show_dialog=True,
        cache_path="token.txt",
        username='Darshil', 
    )
)

response = requests.get(f'https://www.billboard.com/charts/hot-100/{user_answer}/')
billboard_website = response.text
soup = BeautifulSoup(billboard_website,'html.parser')
title_of_song = soup.select(selector='li ul li h3')
songs_name = [names.get_text().strip() for names in title_of_song]
songs_uri = []
user_id = sp.current_user()["id"]
print(user_id)
year = user_answer.split("-")[0]
for songs in songs_name:
    result = sp.search(q=f'track:{songs} year:{year}' ,type='track')
    try:
        uri = result['tracks']['items'][0]['uri']
        songs_uri.append(uri)
    except IndexError:
        print(f'{songs} does not exist in spotify')
playlist = sp.user_playlist_create(user=user_id, name=f"{user_answer} Billboard 100", public=False)
print(playlist)
#Adding songs found into the new playlist
sp.playlist_add_items(playlist_id=playlist["id"], items=songs_uri)