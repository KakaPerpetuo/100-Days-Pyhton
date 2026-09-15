import requests
from bs4 import BeautifulSoup
from ytmusicapi import YTMusic, OAuthCredentials

travel_date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")

URL = f"https://appbrewery.github.io/bakeboard-hot-100/{travel_date}/"

response = requests.get(URL)
website_html = response.text

soup = BeautifulSoup(website_html, "html.parser")
billboard100 = soup.find_all(name="h3", class_="chart-entry__title")

songs_title = [song.getText() for song in billboard100]

client_id = ""
client_secret = ""

ytmusic = YTMusic(
    "oauth.json",
    oauth_credentials=OAuthCredentials(
        client_id=client_id,
        client_secret=client_secret
    )
)

print(ytmusic.get_library_playlists())

playlist_id = ytmusic.create_playlist(
    title=f"{travel_date} - Billboard 100",
    description="Playlist criada com Python",
    privacy_status="PRIVATE"
)

video_ids = []

for song in songs_title:
    resultados = ytmusic.search(song, filter="songs")

    if resultados:
        video_id = resultados[0]["videoId"]
        video_ids.append(video_id)

ytmusic.add_playlist_items(
    playlist_id,
    video_ids
)


