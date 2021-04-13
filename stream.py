import requests
from bs4 import BeautifulSoup, SoupStrainer
import cchardet
import re

def stream_links(link,episode):
	session = requests.Session()
	response = session.get('https://gogoanime.ai' + link + '-episode-' + episode)

	strainer = SoupStrainer('div', attrs={'class' : 'favorites_book'})
	soup = BeautifulSoup(response.content, 'lxml', parse_only=strainer)

	try:
		link = soup.ul.li.a.get('href')

		response_link = session.get(link)
		strainer = SoupStrainer('div', attrs={'class' : 'dowload'})
		soup = BeautifulSoup(response_link.content, 'lxml', parse_only=strainer)

		links = [a['href'] for a in soup.find_all('a', href=True)]
		return links[0]
	except:
		return None