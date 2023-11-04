import tkinter as tk
from tkinter import scrolledtext
import spotipy
import concurrent.futures
from spotipy.oauth2 import SpotifyOAuth
from youtubesearchpython import VideosSearch
from googleapiclient.discovery import build
from google.oauth2 import service_account
from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

def create_spotify_oauth():
    return SpotifyOAuth(
        client_id="86b37e93dbe24f0c86c63f329a22cf70",
        client_secret="00279f7de2974ebb8d36ccda5aade2a8",
        redirect_uri="http://localhost:8888/callback",
        scope="user-library-read"
    )

sp_oauth = create_spotify_oauth()
sp = spotipy.Spotify(auth_manager=sp_oauth)

def get_authenticated_user_channel_id():
    try:
        credentials = service_account.Credentials.from_service_account_file('spotoyou-403820-9eb5975217f9.json', scopes=['https://www.googleapis.com/auth/youtube.force-ssl'])
        developerKey = "AIzaSyD-u_DGVcrSTiMK0gnFvhNCkzGVnxVhNQ0"
        youtube = build('youtube', 'v3', developerKey=developerKey, credentials=credentials)

        channels_response = youtube.channels().list(part='id', mine=True).execute()

        if 'items' in channels_response and channels_response['items']:
            channel_id = channels_response['items'][0]['id']
            return channel_id
        else:
            raise Exception("The user does not have a YouTube channel associated with their account.")
    except Exception as e:
        print(f"Error in get_authenticated_user_channel_id: {str(e)}")
        return None

def create_youtube_playlist(title, description, channel_id):
    credentials = service_account.Credentials.from_service_account_file('spotoyou-403820-9eb5975217f9.json', scopes=['https://www.googleapis.com/auth/youtube.force-ssl'])
    youtube = build('youtube', 'v3', developerKey='AIzaSyD-u_DGVcrSTiMK0gnFvhNCkzGVnxVhNQ0', credentials=credentials)

    playlist = youtube.playlists().insert(
        part="snippet,status",
        body={
            "snippet": {
                "title": title,
                "description": description,
            },
            "status": {
                "privacyStatus": "private",
            },
        }
    ).execute()

    playlist_id = playlist["id"]
    youtube.playlists().insert(
        part="snippet",
        body={
            "id": playlist_id,
            "snippet": {
                "channelId": channel_id,
            },
        }
    ).execute()

    return playlist_id

def get_video_id_from_url(url):
    if 'youtube.com/watch' in url:
        video_id = url.split('?v=')[1]
        return video_id
    else:
        return None

def add_video_to_playlist(playlist_id, video_url):
    video_id = get_video_id_from_url(video_url)
    if video_id:
        credentials = service_account.Credentials.from_service_account_file('spotoyou-403820-9eb5975217f9.json', scopes=['https://www.googleapis.com/auth/youtube.force-ssl'])
        youtube = build('youtube', 'v3', developerKey='AIzaSyD-u_DGVcrSTiMK0gnFvhNCkzGVnxVhNQ0', credentials=credentials)

        youtube.playlistItems().insert(
            part="snippet",
            body={
                "snippet": {
                    "playlistId": playlist_id,
                    "resourceId": {
                        "kind": "youtube#video",
                        "videoId": video_id,
                    },
                },
            }
        ).execute()

def display_user_playlists():
    playlists = sp.current_user_playlists()
    playlist_links = []

    for playlist in playlists['items']:
        playlist_name = playlist['name']
        playlist_uri = playlist['uri']
        playlist_links.append((playlist_name, playlist_uri))

    return playlist_links

def copy_to_clipboard(text):
    fenetre.clipboard_clear()
    fenetre.clipboard_append(text)
    fenetre.update()

def display_playlists_with_links():
    playlist_links = display_user_playlists()
    text_area.delete('1.0', tk.END)
    for playlist_name, playlist_uri in playlist_links:
        text_area.insert(tk.END, f"{playlist_name} - {playlist_uri}\n")


def convert_playlist():
    result_label.config(text="Converting...")
    fenetre.update_idletasks()
    playlist_url = url_entry.get()

    try:
        playlists = sp.current_user_playlists()
        videos = []

        def search_and_append_video(track):
            song = track['track']['name']
            artist = track['track']['artists'][0]['name']
            search_query = f"{song} {artist} site:youtube.com"
            videos_search = VideosSearch(search_query, limit=1)
            results = videos_search.result()
            if results['result']:
                video = results['result'][0]
                videos.append(video['link'])

        with concurrent.futures.ThreadPoolExecutor() as executor:
            executor.map(search_and_append_video, (track for playlist in playlists['items'] for track in sp.playlist_tracks(playlist['id'])['items']))

        videos = list(set(videos))

        playlist_title = 'Playlist converted from Spotify'
        playlist_description = 'Playlist created from Spotify songs'
        channel_id = 'UCecUjbVDxmL1yQwZJDzReAQ'
        if channel_id is not None:
            playlist_id = create_youtube_playlist(playlist_title, playlist_description, channel_id)

            for video_url in videos:
                add_video_to_playlist(playlist_id, video_url)

            result_label.config(text="Playlist converted successfully")
            display_playlists_with_links()
        else:
            result_label.config(text="Error: Unable to get user's YouTube channel ID")

    except Exception as e:
        result_label.config(text=f"Error: {str(e)}")

fenetre = tk.Tk()
fenetre.title("Spotify to YouTube Playlist Converter")

title_label = tk.Label(fenetre, text="Spotify to YouTube Playlist Converter")
title_label.pack()

text_area = scrolledtext.ScrolledText(fenetre, width=40, height=10)
text_area.pack()

show_playlists_button = tk.Button(fenetre, text="Show My Playlists", command=display_playlists_with_links)
show_playlists_button.pack()

copy_button = tk.Button(fenetre, text="Copy URI to Clipboard", command=lambda: copy_to_clipboard(text_area.get("1.0", tk.END)))
copy_button.pack()


url_label = tk.Label(fenetre, text="Spotify Playlist URL:")
url_label.pack()

url_entry = tk.Entry(fenetre)
url_entry.pack()

convert_button = tk.Button(fenetre, text="Convert", command=convert_playlist)
convert_button.pack()

result_label = tk.Label(fenetre, text="")
result_label.pack()

fenetre.mainloop()
