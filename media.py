import webbrowser

class Movie():
    VALID_RATINGS = ["G","PG","PG13","R"]

    def __init__(self, movie_title, poster_image, trailer_youtube, release_date):
        self.title = movie_title
        #self.overview = overview
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
        self.release_date = release_date


    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)


