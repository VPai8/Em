import requests
import time
from bs4 import BeautifulSoup


header={ "Authorization":"Bearer " + "insert your client_access_token here",
     "User-Agent": ""
     }

def lyrics(song_lyrics_url):
  page = requests.get(song_lyrics_url)
  soup = BeautifulSoup(page.text, "html.parser")
  [h.extract() for h in soup('script')]
  lyrics = soup.find("div" , class_="lyrics").get_text()
  return lyrics

def syncreq(page):
 time.sleep(100)
 x=0
 response = requests.get(query,headers=header,data={'sort':'popularity','per_page': 50,'page': page})
 result = response.json()
 print(result)
 for song in result['response']['songs']:
   x=x+1
   print(x)
   print(song['full_title'])
   f.write(lyrics(song['url'])+"\n")

query = "https://api.genius.com/artists/45/songs"
f = open('lyrics.txt', 'a')
for page in range(1,5):
 syncreq(page) 
