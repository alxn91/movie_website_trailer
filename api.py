import urllib2
import json

"""Function pulls movie info"""


def get_info(query):
    """create variable to store api key"""
    api_key = 'cc4b67c52acb514bdf4931f7cedfd12b'
    """url to look for movie info"""
    url = 'http://api.themoviedb.org/3/search/movie?api_key=' + api_key
    movie_title = query.replace(' ', '%20')
    final_url = url + "&query=" + movie_title.lower()
    """open url and create json file"""
    json_obj = urllib2.urlopen(final_url)
    data = json.load(json_obj)
    """return information about the movie"""
    return data

"""function to get title of movie"""


def get_title(query):
    """call function get_info with provided movie title and store data in variable"""  # NOQA
    data = get_info(query)
    """loop through items in results dic"""
    for key in data['results']:
        """look for a match with provided movie title"""
        if key['title'] == query:
            """return movie title if match found"""
            return key['title']

"""function to get release date"""


def get_release_date(query):
    """call function get_info with provided movie title and store data in variable"""  # NOQA
    data = get_info(query)
    """loop through items in results dic"""
    for title in data['results']:
        """look for a match with provided movie title"""
        if title['title'] == query:
            """return relase date if match found"""
            return title['release_date']

"""function to get poster image"""


def get_poster(query):
    """call function get_info with provided movie title and store data in variable"""  # NOQA
    data = get_info(query)
    """loop through items in results dic"""
    for title in data['results']:
        """look for a match with provided movie title"""
        if title['title'] == query:
            """return poster image path if match found"""
            return "https://image.tmdb.org/t/p/w500/" + title['poster_path']

"""function to get rating"""


def get_rating(query):
    """call function get_info with provided movie title and store data in variable"""  # NOQA
    data = get_info(query)
    """loop through items in results dic"""
    for title in data['results']:
        """look for a match with provided movie title"""
        if title['title'] == query:
            """return vote average(rating) if match found"""
            return title['vote_average']

