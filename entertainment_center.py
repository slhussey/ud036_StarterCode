import media
import fresh_tomatoes

# create instace of Movie for Toy Story
toy_story = media.Movie("Toy Story",
                        "A story of a boy and his toys that come to life",
                        "http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=vwyZH85NQC4")

# and one for Avatar
avatar = media.Movie("Avatar",
                     "A marine on an alien planet",
                     "http://upload.wikimedia.org/wikipedia/id/b/b0/Avatar-Teaser-Poster.jpg",
                     "http://www.youtube.com/watch?v=-9ceBgWV8io")

# and Top Gun
my_movie = media.Movie("Top Gun",
                       "Top naval pilot school",
                       "https://www.google.com/imgres?imgurl=http%3A%2F%2Fwww.joblo.com%2Fposters%2Fimages%2Ffull%2F1986-top-gun-poster1.jpg&imgrefurl=http%3A%2F%2Fwww.joblo.com%2Fmovie-posters%2F1986%2Ftop-gun&docid=UMW4dVUPK22X0M&tbnid=FocR7vkaLuPRkM%3A&vet=10ahUKEwiii9n0usvVAhUE5YMKHRU4A8oQMwi1ASgZMBk..i&w=580&h=872&bih=832&biw=1554&q=top%20gun%20poster&ved=0ahUKEwiii9n0usvVAhUE5YMKHRU4A8oQMwi1ASgZMBk&iact=mrc&uact=8",
                       "https://www.youtube.com/watch?v=qAfbp3YX9F0")

# and School of Rock
school_of_rock = media.Movie("School of Rock",
                             "Storyline",
                             "http://upload.wikimedia.org/wikipedia/en/l/l1/School_of_Rock_Poster.jpg",
                             "https://www.youtube.com/watch?v=3PsUJFEBC74")

# and Ratatouille
ratatouille = media.Movie("Ratatouille",
                          "Storyline",
                          "http://upload.wikimedia.org/wikipedia/en/S/SO/RatatouillePoster.jpg",
                          "https://www.youtube.com/watch?v=c3sBBRxDAqk")

# and Midnight in Paris
midnight_in_paris = media.Movie("Midnight in Paris",
                                "Storyline",
                                "http://upload.wikimedia.org/wikipedia/en/9/9f/Midnight_in_Paris_Poster.jpg",
                                "https://www.youtube.com/watch?v=atLg2wQQxvU")

# and Hunger Games
hunger_games = media.Movie("Hunger Games",
                           "Storyline",
                           "http://upload.wikimedia.org/wikipedia/en/4/42/HungerGamesPoster.jpg",
                           "https://www.youtube.com/watch?v=PbA63a7H0bo")

# create list of all movies to feed to the web page generator
movies = [toy_story, avatar, school_of_rock, ratatouille, midnight_in_paris, hunger_games]

# generate webpage and display it
fresh_tomatoes.open_movies_page(movies)
