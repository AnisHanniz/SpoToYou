from setuptools import setup, find_packages

requires = [
    'tk',  # tkinter est inclus dans la bibliothèque standard de Python, pas besoin de le spécifier ici
    'spotipy',
    'html5lib',
    'youtubesearchpython',
    'google-api-python-client',
    'google-auth',
    'requests',
    'requests-html',
    'beautifulsoup4',
    'youtube-dl',
    'pathlib',
    'pandas'
]

setup(
    name='SpoToYou',
    version='1.0',
    description='An application that converts your Spotify playlists to YouTube playlists',
    author='Anis HANNIZ',
    author_email='hanniz.n.anis@gmail.com',
    keywords='web flask',
    packages=find_packages(),
    include_package_data=True,
    install_requires=requires
)
