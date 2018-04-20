import webbrowser 

class Movie(object):
	"""Creates objects that contains critical information about a movie, including a trailer"""
	#Constructor
	def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):
	    self.title = movie_title 
	    self.storyline = movie_storyline
	    self.poster_image_url = poster_image
	    self.trailer_youtube_url = trailer_youtube

	#This function opens a movie trailer as a container in the same web page (rather than new tab)
	def show_trailer(self):
	    webbrowser.open(self.trailer_youtube_url)