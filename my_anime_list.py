from mal import *
from bs4 import BeautifulSoup, SoupStrainer
import requests
import re

def details(anime_name):
	dub = False
	if '(Dub)' in anime_name:
		anime_name = anime_name.replace('(Dub)', '')
		dub = True
	output = []
	search = AnimeSearch(anime_name)
	selected = search.results[0]
	title = selected.title
	total_episodes = str(selected.episodes)
	if total_episodes == 'None' or dub:
		session = requests.Session()
		link = re.sub("[^0-9a-zA-Z]+", "", title).lower()
		if dub:
			link = link + 'dub'
		try:
			response = session.get('https://www1.gogoanime.ai/category/' + link)
			strainer = SoupStrainer('div', attrs={'class': 'anime_video_body'})
			soup = BeautifulSoup(response.content, 'lxml', parse_only=strainer)
			total_episodes = soup.find('ul', id="episode_page").findAll('li')
			total_episodes = total_episodes[-1].find('a')['ep_end']
		except:
			total_episodes = 'None'
	score = str(selected.score)
	anime_type = selected.type
	detail = {'title':title, 'total_episodes':total_episodes, 'score':score, 'anime_type':anime_type}
	output.append(detail)
	return(output)

