import webbrowser


class Movie(object):
    """
    Creates an object that represents a movie

    Object contains critical information about a movie for a trailer website,
    including the title, storyline, poster image URL, and Youtube trailer URL.

    Also included is functionality to open the Youtube trailer within the
    same window.

    Parameters
    ----------
    movie_title : str
        The title of the movie
    movie_storyline : str
        A quick summary of the storyline of the movie
    poster_image : str
        URL to Wikimedia's image on file
    trailer_youtube : str
        URL to Youtube's trailer video for the movie

    Attributes
    ----------
    title : str
        The title of the movie
    storyline : str
        A quick summary of the storyline of the movie
    poster_image_url : str
        URL to Wikimedia's image on file
    trailer_youtube_url : str
        URL to Youtube's trailer video for the movie
    """

    def __init__(self, movie_title, movie_storyline,
                 poster_image, trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        """
        Opens a movie trailer as a container
        in the same web page (rather than new tab)

        Parameters
        ----------
        None

        Returns
        -------
        None
        """
        webbrowser.open(self.trailer_youtube_url)
