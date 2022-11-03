import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import pandas as pd
import numpy as np
cid = '21fdb3d7196f40498694850370c60ade'
secret = 'ca86ad661abf4530a9c83f48b6d12124'
client_credentials_manager = SpotifyClientCredentials(client_id=cid, client_secret=secret)
sp = spotipy.Spotify(client_credentials_manager = client_credentials_manager)

playlist_link = ['https://open.spotify.com/playlist/37i9dQZEVXbKPTKrnFPD0G?si=03434d53bc6d43b5']
playlist_URI = playlist_link.split("/")[-1].split("?")[0]
track_uri = []
track_name = []
artist_uri =[]
artist_name =[]
artist_fame =[]
artist_gen =[]
track_fame=[]
for i in range(9):
    for track in sp.playlist_tracks(playlist_URI, offset = 100*i)["items"]:
        #URI
        track_uri.append(track["track"]["uri"])

        #Track name
        track_name.append(track["track"]["name"])

        #Main Artist
        au = track["track"]["artists"][0]["uri"]
        artist_uri.append(au)
        ai = sp.artist(au)
        #Name, popularity, genre
        artist_name.append(track["track"]["artists"][0]["name"])
        artist_fame.append(ai["popularity"])
        artist_gen.append(ai["genres"])

        #Popularity of the track
        track_fame.append(track["track"]["popularity"])
        
danceability = []
energy =[]
key =[]
loudness =[]
speechiness =[]
acousticness=[]
instrumentalness = []
tempo = []
duration = []

for track in track_uri:
    s = sp.audio_features(track)
    danceability.append(s[0]['danceability'])
    energy.append(s[0]['energy'])
    key.append(s[0]['key'])
    loudness.append(s[0]['loudness'])
    speechiness.append(s[0]['speechiness'])
    acousticness.append(s[0]['acousticness'])
    instrumentalness.append(s[0]['instrumentalness'])
    tempo.append(s[0]['tempo'])
    duration.append(s[0]['duration_ms'])

# Coachella
# 1. correlation between energy and loudness
# 2. key has no correlation to any variables, scatter evenly in the distribution (except key = 3 big drop)
# 3. speechiness negative correlation with instrumentalness and acousticness
# 4. more popularity at high danceability and enregy compared to low
# 5. popular with less instrumentalness and less acousticness
# 6. more speechiness means more danceability
# 7. energy negative correlation with acousticness
# 8. loudness and energy is high correlated
# 9. most of the song is in -4 to -9 in loudness
# 10. remove loudenss(correlated with energy)variables