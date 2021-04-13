from flask import Flask, request, jsonify
import requests
from bs4 import BeautifulSoup, SoupStrainer
import cchardet
import re
from search import search_anime
from my_anime_list import details
from stream import stream_links

app = Flask(__name__)

@app.route('/search',methods=['GET'])
def search():
	search = request.args.get('search')
	if request.method == 'GET':
		output = search_anime(search)
	return jsonify(output)
@app.route('/anime',methods=['GET'])
def anime():
	anime_name = request.args.get('anime')
	if request.method == 'GET':
		anime_details =  details(anime_name)
	return jsonify(anime_details)
@app.route('/episode',methods=['GET'])
def episode():
	link = request.args.get('link')
	episode = request.args.get('episode')
	if request.method == 'GET':
		stream_link = stream_links(link,episode)
	return jsonify(stream_link)

if __name__ == '__main__':
	app.run(host="0.0.0.0",)