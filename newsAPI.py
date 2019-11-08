# q = query_term
# sortBy = {'relevancy', 'publishedAt', 'popularity'}
# from = YYYY-MM-DD
# to = YYYY-MM-DD
# categories =  {'sports', 'entertainment', 'science', 'business', 'health', 'technology', 'general'}

from key import api_key
from misc import match_article_query
from sources import valid_sources
import requests
import json

def newsAPI_json(search_terms):
	url = 'https://newsapi.org/v2/top-headlines?'	
	for key, value in search_terms.items():
		url+= "{}={}&".format(key, value)
	url += "apiKey=" + api_key
	contents = requests.get(url);

	return contents.text

def newsAPI_content(search_terms):
	# Number of results = json.totalResults
	# source_name = json.articles[n].source.name
	# url = json.articles[n].url
	objJSON = json.JSONDecoder().decode(newsAPI_json(search_terms))
	results = objJSON['totalResults']

	sources = []
	url = []
	title = []

	if(results!=0):
		sources = [i['source']['name'] for i in objJSON['articles'] if(i['source']['id'] in valid_sources)]
		url = [i['url'] for i in objJSON['articles'] if(i['source']['id'] in valid_sources)]	
		title = [i['title'] for i in objJSON['articles'] if(i['source']['id'] in valid_sources)]	

	return (results, sources, url, title)

def newsAPI_json_everything(search_terms):
	url = 'https://newsapi.org/v2/everything?'	
	for key, value in search_terms.items():
		url+= "{}={}&".format(key, value)
	url += "apiKey=" + api_key 
	contents = requests.get(url);	

	return contents.text

def newsAPI_content_everything(search_terms):
	# Number of results = json.totalResults
	# source_name = json.articles[n].source.name
	# url = json.articles[n].url
	objJSON = json.JSONDecoder().decode(newsAPI_json_everything(search_terms))
	results = objJSON['totalResults']	
	
	sources = []
	url = []
	title = []

	if(results!=0):		
		results = 0;
		for i in objJSON['articles']:
			if(i['source']['id'] in valid_sources):
				keywords = (i['title'] + ' ' + i['description'])	
				if(match_article_query(search_terms['q'].lower().split('+'), keywords)):			#check how close the article title and description match the search query
					sources.append(i['source']['name'])
					url.append(i['url'])
					title.append(i['title'])
					results+=1;
	return (results, sources, url, title)