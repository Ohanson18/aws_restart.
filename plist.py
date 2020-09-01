import requests
from bs4 import BeautifulSoup

r = requests.get('https://www.bbc.co.uk/programmes/articles/5JDPyPdDGs3yCLdtPhGgWM7/bbc-radio-6-music-playlist')
soup = BeautifulSoup(r.text, 'html.parser')

songs = []

for item in soup.find_all('p'):
  if ' - ' in str(item.string):
    song = str(item.string).split('-')
    song_dict = {}
    song_dict['Artist'] = song[0]
    song_dict['Title'] = song[1]
    songs.append(song_dict)
for song in songs:
    print("Artist: " + song['Artist'] + "\t\t\tSong: " + song['Title'])
