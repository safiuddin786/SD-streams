import requests
from bs4 import BeautifulSoup, SoupStrainer
import cchardet
import re

def search_anime(search_data):
	output = []
	session = requests.Session()
	try:
		response = session.get('https://www1.gogoanime.ai//search.html?keyword=' + search_data)

		strainer = SoupStrainer('div', attrs={'class' : 'last_episodes'})
		soup = BeautifulSoup(response.content, 'lxml', parse_only=strainer)
		
		for temp in soup.find_all('li'):
			data = {}
			title = temp.find('a', title=True)['title']
			link = temp.find('a', href=True)['href']
			link = re.findall('/category(.*)', link)[0]
			img = temp.find('div', class_='img').a.img['src']
			try:
				release = re.search('Released: .*\S',temp.find('p', class_='released').string)
			except:
				release = 'N/A'
			data['title'] = str(title)
			data['link'] = str(link)
			data['img'] = str(img)
			data['release'] = str(release.group(0))
			output.append(data)
		return output
		# search_anime('naruto')

	except:
		return None