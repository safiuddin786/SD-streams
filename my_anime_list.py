from mal import *

def details(anime_name):
	search = AnimeSearch(anime_name)
	selected = search.results[0]
	title = selected.title
	total_episodes = selected.episodes
	score = selected.score
	anime_type = selected.type
	detail = {'title':title, 'total_episodes':total_episodes, 'score':score, 'anime_type':anime_type}
	return(detail)

