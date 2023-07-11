from bs4 import BeautifulSoup
import requests
from datetime import datetime
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from main_artisti import Artists
from pprint import pprint

client_id = ""
client_secret = ""
user_id = ''
redirect_uri = "http://example.com"


year_to_travel = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")
only_year = year_to_travel[:4]

if '-' in year_to_travel:
    songs = requests.get(f"https://www.billboard.com/charts/hot-100/{year_to_travel}/")
    songs_page = songs.text
else:
    date_object = datetime.strptime(year_to_travel, "%Y %m %d")
    output_string = date_object.strftime("%Y-%m-%d")
    songs = requests.get(f"https://www.billboard.com/charts/hot-100/{output_string}/")
    songs_page = songs.text

soup = BeautifulSoup(songs_page,'html.parser')
artists = Artists(soup)
all_artists = artists.artists()


headings = soup.select(selector="li ul li h3")
#LIST OF HUNDRED SONGS IN A LIST
hundred_songs = [x.getText().strip() for x in headings]


sp_oauth = SpotifyOAuth(
    scope="playlist-modify-private",
    client_id=client_id,
    client_secret=client_secret,
    redirect_uri="http://example.com",
    username='Marus'
    )


sp = spotipy.Spotify(auth_manager=sp_oauth)

song_uris = []
for song in hundred_songs:
    result = sp.search(q=f'year:{only_year} track:{song}',type='track')
    print(result)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
        print(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")

name = 'Yes sir'

playlist = sp.user_playlist_create(user=user_id, name=f'{year_to_travel} Billboard 100', public=False)
print(playlist)

sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)









