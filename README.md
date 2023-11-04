FR : 

# Convertisseur de Playlists Spotify en Playlists YouTube

Cette application est un simple programme Python qui vous permet de convertir vos playlists Spotify en playlists YouTube. Elle utilise l'API Spotify, l'API YouTube et diverses bibliothèques pour rechercher et ajouter des vidéos YouTube à une nouvelle playlist YouTube.

## Exigences

Avant d'utiliser cette application, vous devez configurer quelques éléments :

1. **Clé API Spotify :** Vous devez créer une application de développement Spotify et obtenir un ID client et un secret client. Remplacez les espaces réservés dans la fonction `create_spotify_oauth()` par vos informations d'identification.

2. **Clé API YouTube :** Vous avez besoin d'une clé API YouTube. Remplacez la valeur de `developerKey` dans les fonctions `get_authenticated_user_channel_id()`, `create_youtube_playlist()` et `add_video_to_playlist()` par votre clé API YouTube.

3. **Fichier JSON de Compte de Service Google :** Vous avez besoin d'un fichier JSON de compte de service pour l'API YouTube. Remplacez le chemin du fichier dans les fonctions `get_authenticated_user_channel_id()`, `create_youtube_playlist()` et `add_video_to_playlist()` par le chemin de votre fichier JSON.

4. **Flask et Flask-CORS :** Cette application utilise Flask pour mettre en place un serveur web simple. Installez Flask et Flask-CORS avec `pip install flask flask-cors`.

5. **Autres bibliothèques requises :** Installez les bibliothèques Python requises avec `pip install spotipy youtubesearchpython google-api-python-client`.

## Utilisation

1. Après avoir configuré les exigences, exécutez le script Python.

```bash
python nom_de_votre_script.py
```

2. La fenêtre GUI apparaîtra. Vous verrez les composants suivants :

   - Étiquette de titre : "Convertisseur de Playlists Spotify en Playlists YouTube"
   - Zone de texte : Affiche les noms et les URI de vos playlists Spotify.
   - Bouton "Afficher Mes Playlists" : Cliquez pour afficher vos playlists Spotify.
   - Bouton "Copier l'URI dans le Presse-Papiers" : Copie les URI dans le presse-papiers.
   - Étiquette d'URL : "URL de la Playlist Spotify"
   - Entrée d'URL : Entrez l'URL de votre playlist Spotify.
   - Bouton "Convertir" : Convertit votre playlist Spotify en playlist YouTube.
   - Étiquette de résultat : Affiche l'état de la conversion.

3. Cliquez sur "Afficher Mes Playlists" pour afficher vos playlists Spotify et leurs URI.

4. Saisissez l'URL de votre playlist Spotify dans le champ "URL de la Playlist Spotify".

5. Cliquez sur le bouton "Convertir" pour démarrer le processus de conversion. L'application recherchera les vidéos YouTube correspondantes et créera une nouvelle playlist YouTube avec ces vidéos. Le résultat sera affiché dans l'"Étiquette de Résultat".

6. Si la conversion réussit, l'URL de votre nouvelle playlist YouTube sera affichée dans l'"Étiquette de Résultat".

## Notes Importantes

- L'application utilise les API Spotify et YouTube. Veuillez prendre connaissance de leurs termes et conditions d'utilisation.

- Assurez-vous de conserver en sécurité votre fichier JSON de compte de service Google, votre clé API YouTube et vos identifiants d'API Spotify et de ne pas les partager.

- Cette application est un exemple de base et peut ne pas couvrir tous les cas particuliers. N'hésitez pas à la modifier et à l'étendre pour mieux répondre à vos besoins.

Profitez de la conversion de vos playlists Spotify en playlists YouTube en toute simplicité !


Eng :

# Spotify to YouTube Playlist Converter

This application is a simple Python program that allows you to convert your Spotify playlists into YouTube playlists. It uses the Spotify API, YouTube API, and various libraries to search for and add YouTube videos to a new YouTube playlist.

## Requirements

Before using this application, you need to set up a few things:

1. **Spotify API Key:** You need to create a Spotify developer application and obtain a client ID and client secret. Replace the placeholders in the `create_spotify_oauth()` function with your credentials.

2. **YouTube API Key:** You need a YouTube API key. Replace the `developerKey` value in the `get_authenticated_user_channel_id()`, `create_youtube_playlist()`, and `add_video_to_playlist()` functions with your YouTube API key.

3. **Google Service Account JSON File:** You need a service account JSON file for the YouTube API. Replace the file path in the `get_authenticated_user_channel_id()`, `create_youtube_playlist()`, and `add_video_to_playlist()` functions with the path to your JSON file.

4. **Flask and Flask-CORS:** This application uses Flask to set up a simple web server. Install Flask and Flask-CORS using `pip install flask flask-cors`.

5. **Other Required Libraries:** Install the required Python libraries using `pip install spotipy youtubesearchpython google-api-python-client`.

## Usage

1. After setting up the requirements, run the Python script.

```bash
python your_script_name.py
```

2. The GUI window will appear. You will see the following components:

   - Title Label: "Spotify to YouTube Playlist Converter"
   - Text Area: Displays your Spotify playlists' names and URIs.
   - "Show My Playlists" Button: Click to display your Spotify playlists.
   - "Copy URI to Clipboard" Button: Copies the URIs to your clipboard.
   - URL Label: "Spotify Playlist URL"
   - URL Entry: Enter the URL of your Spotify playlist.
   - "Convert" Button: Converts your Spotify playlist to YouTube.
   - Result Label: Displays the conversion status.

3. Click "Show My Playlists" to display your Spotify playlists and their URIs.

4. Enter the URL of your Spotify playlist in the "Spotify Playlist URL" field.

5. Click the "Convert" button to start the conversion process. The application will search for the corresponding YouTube videos and create a new YouTube playlist with those videos. The result will be displayed in the "Result Label."

6. If the conversion is successful, your new YouTube playlist's URL will be displayed in the "Result Label."

## Important Notes

- The application makes use of the Spotify and YouTube APIs. Please be aware of their usage terms and conditions.

- Make sure your Google service account JSON file, YouTube API key, and Spotify API credentials are kept secure and not shared.

- This application is a basic example and might not cover all edge cases. Feel free to modify and extend it to better suit your needs.

Enjoy converting your Spotify playlists to YouTube playlists with ease!
