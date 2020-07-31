from bs4 import BeautifulSoup
import requests
from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.dbsparta
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}

data = requests.get('https://www.genie.co.kr/chart/top200?ditc=D&rtm=N&ymd=20200713',headers=headers)
soup = BeautifulSoup(data.text, 'html.parser')
musics_lst = soup.select('#body-content > div.newest-list > div > table > tbody > tr')
for music in musics_lst :
    rank = music.select_one('td.number').text.split()[0]
    name = music.select_one('a.title.ellipsis').text.strip()
    artist = music.select_one('a.artist.ellipsis').text
    print(rank,name,artist)