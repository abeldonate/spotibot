from dotenv import load_dotenv
import json
import os
import spotipy
from spotipy.oauth2 import SpotifyOAuth


load_dotenv()

client_id = os.getenv("CLIENT_ID")
client_secret = os.getenv("CLIENT_SECRET")
redirect_uri = 'http://localhost:8090'
scope = 'user-library-read user-top-read user-follow-read'

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=client_id, client_secret=client_secret, redirect_uri=redirect_uri, scope=scope))


# Get my followed artists
def get_followed_artists():
    top_artists = sp.current_user_followed_artists(limit=3)
    artist_list = list()
    for idx, artist in enumerate(top_artists['artists']['items']):
        artist_list.append([artist['name'], artist['id']])
    return artist_list 

# Given an artist, get the albums
def get_artist_albums(artist):
    artist_name = artist[0]
    artist_id = artist[1]
    albums = sp.artist_albums(artist_id, limit=4)
    album_list = list()
    for idx, album in enumerate(albums['items']):
        album_list.append(album['name'])
    return album_list

def artists_to_json(artists_list):
    data = dict()
    for artist in artists_list:
        album_list = get_artist_albums(artist)
        data[artist[0]] = album_list
    return data

def get_new_releases():
    artists_list = get_followed_artists()
    new_data = artists_to_json(artists_list)

    # Read the old_data in json data/data.json
    with open('data/data.json', 'r') as f:
        old_data = json.loads(f.read())

    new_releases = dict()
    for artist in new_data:
        if artist not in old_data:
            new_releases[artist] = new_data[artist]
        else:
            new_releases[artist] = [album for album in new_data[artist] if album not in old_data[artist]]
            if(len(new_releases[artist]) == 0):
                new_releases.pop(artist)

    with open('data/data.json', 'w') as f:
        f.write(json.dumps(new_data))

    return new_releases



