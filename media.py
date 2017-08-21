import webbrowser

"""Creat a class with named Movie"""
class Movie():
    """initalize variables when class called"""
    def __init__(self,
                 movie_title,
                 poster_image,
                 trailer_youtube,
                 release_date,
                 rating):
        self.title = movie_title
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
        self.release_date = release_date
        self.rating = rating
    """function to open movie trailer"""
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)

