import media
import fresh_tomatoes


# Instantiating 6 members of class Movie, which are my fave movies
freaknik = media.Movie("Freaknik the Musical",
                       "A drunk ghost does some things and sings",
                       "https://upload.wikimedia.org/wikipedia/en/9/99/"
                       "Freaknik_-_The_Musical.jpg",
                       "https://www.youtube.com/watch?v=zXo_1ba34aE")

getout = media.Movie("Hurricane Bianca",
                     "A drag queen teaching school",
                     "https://upload.wikimedia.org/wikipedia/en/2/2f/"
                     "Hurricane_Bianca_Poster_2.png",
                     "https://www.youtube.com/watch?v=q0a72wkqlqU")

delicatessen = media.Movie("Delicatessen",
                           "A post-apocalyptic comedy; when meat becomes so "
                           "rare that it is used as currency",
                           "https://upload.wikimedia.org/wikipedia/en/0/04/"
                           "Delicatessen2.jpg",
                           "https://www.youtube.com/watch?v=Tg3V8HDK5go")

beingjohn = media.Movie("Being John Malkovich",
                        "Weird tube world",
                        "https://upload.wikimedia.org/wikipedia/en/5/55/Being"
                        "_John_Malkovich_poster.jpg",
                        "https://www.youtube.com/watch?v=2UuRFr0GnHM")

thief = media.Movie("The Thief and the Cobbler",
                    "A pesky thief steals gold balls",
                    "https://upload.wikimedia.org/wikipedia/en/3/34/"
                    "Thiefwilliamsposter.jpg",
                    "https://www.youtube.com/watch?v=HMORDgnxNs8")

moonlight = media.Movie("Moonlight",
                        "A tough upbringing can make for a great movie!",
                        "https://upload.wikimedia.org/wikipedia/en/8/84/"
                        "Moonlight_%282016_film%29.png",
                        "https://www.youtube.com/watch?v=9NJj12tJzqc")

# Creating a list of all my favorite movies
movies = [freaknik, getout, delicatessen, beingjohn, thief, moonlight]

# This actually opens up the newly generated webpage!
fresh_tomatoes.open_movies_page(movies)
