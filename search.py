import requests
import requests_random_user_agent
from bs4 import BeautifulSoup, SoupStrainer
import re

def search_anime(search_data):
	output = []
	session = requests.Session()
	try:
		response = session.get('https://gogoanime.pe//search.html?keyword=' + search_data)

		strainer = SoupStrainer('div', attrs={'class' : 'last_episodes'})
		soup = BeautifulSoup(response.content, 'lxml', parse_only=strainer)
		
		for temp in soup.find_all('li'):
			data = {}
			title = temp.find('a', title=True)['title']
			link = temp.find('a', href=True)['href']
			link = re.findall('/category(.*)', link)[0]
			img = temp.find('div', class_='img').a.img['src']

			check = temp.find('p', class_='released').string
			if(re.sub("[^0-9a-zA-Z]+", "", check) == ''):
				release = 'N/A'
			else:
				release = re.search('Released: .*\S',check).group(0)

			data['title'] = str(title)
			data['link'] = str(link)
			data['img'] = str(img)
			data['release'] = str(release)
			output.append(data)
		return output
		# search_anime('naruto')

	except:
		return None