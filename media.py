import webbrowser


class Movie():
    """ Class to retain details about a movie so that a web page can
    be created with a list of several movies """

    # initialize instance variables
    def __init__(self,
                 movie_title,
                 movie_storyline,
                 poster_image,
                 trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    # display the video of the trailer via web browser
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
