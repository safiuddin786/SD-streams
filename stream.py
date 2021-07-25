import requests
from bs4 import BeautifulSoup, SoupStrainer
import re

def stream_links(link,episode):
	session = requests.Session()
	response = session.get('https://gogoanime.pe/' + link + '-episode-' + episode)

	strainer = SoupStrainer('div', attrs={'class' : 'anime_video_body'})
	soup = BeautifulSoup(response.content, 'lxml', parse_only=strainer)

	try:
		links = {}
		
		x = soup.find('div', attrs={'class': 'anime_muti_link'})
		temp = x.find('ul').findAll('li')
		for t in temp:
			type = t.get('class')[0]
			link = t.find('a')['data-video']
			links[type] = link
		return links
	except:
		return None