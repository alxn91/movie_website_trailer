import urllib2
import json


def get_info(query):
    
    tmbd_api = 'cc4b67c52acb514bdf4931f7cedfd12b'
    
    url = 'http://api.themoviedb.org/3/search/movie?api_key=' + tmbd_api
    movie_title = query.replace(' ', '%20')
    final_url = url + "&query=" + movie_title.lower()
    
    json_obj = urllib2.urlopen(final_url)
    data = json.load(json_obj)
    
    return data


def get_title(query):
    
    data = get_info(query)
    
    for key in data['results']:
        if key['title'] == query:
            return key['title']


def get_release_date(query):
    
    data = get_info(query)
    
    for title in data['results']:
        if title['title'] == query:
            return title['release_date']


def get_overview(query):
    data = get_info(query)
    
    for title in data['results']:
        if title['title'] == query:
            return title['overview']


def get_poster(query):
    data = get_info(query)
    
    for title in data['results']:
        if title['title'] == query:
            return "https://image.tmdb.org/t/p/w500/" + title['poster_path']


def get_rating(query):
    data = get_info(query)

    for title in data['results']:
        if title['title'] == query:
            return title['vote_average']
