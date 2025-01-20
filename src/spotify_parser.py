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
    artist_list = list()
    while True:
        response = sp.current_user_followed_artists(limit=30,after=artist_list[-1][1] if len(artist_list) > 0 else None)
        if len(response['artists']['items']) == 0:
            return artist_list
        for artist in response['artists']['items']:
            artist_list.append([artist['name'], artist['id']])


# Given an artist, get the albums
def get_artist_albums(artist):
    artist_id = artist[1]
    album_list = list()
    while True:
        response = sp.artist_albums(artist_id, limit=50, offset=len(album_list))
        if len(response['items']) == 0:
            return album_list
        for album in response['items']:
            album_list.append(album['name'])

# Convert the list of artist to a dictionary with all the albums
def artists_to_dict(artists_list):
    data = dict()
    for artist in artists_list:
        album_list = get_artist_albums(artist)
        data[artist[0]] = album_list
    return data

# Get the new releases from the artists I follow. Write the new data with the current albums
def get_new_releases():
    artists_list = get_followed_artists()
    new_data = artists_to_dict(artists_list)

    # Read the old_data in json data/data.json
    with open('data/data.json', 'r') as f:
        old_data = json.loads(f.read())

    new_releases = dict()
    for artist in new_data:
        if artist in old_data:
            if len(new_data[artist]) > len(old_data[artist]):
                new_releases[artist] = [album for album in new_data[artist] if album not in old_data[artist]]

    with open('data/data.json', 'w') as f:
        f.write(json.dumps(new_data))

    return new_releases


#print(get_followed_artists())



