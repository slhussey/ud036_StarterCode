import media
import fresh_tomatoes

# create instace of Movie for Toy Story
toy_story = media.Movie(
        "Toy Story",
        "A story of a boy and his toys that come to life",
        "http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
        "https://www.youtube.com/watch?v=vwyZH85NQC4")

# and one for Avatar
avatar = media.Movie(
        "Avatar",
        "A marine on an alien planet",
        "https://goo.gl/M2K3YD",
        "http://www.youtube.com/watch?v=-9ceBgWV8io")

# and Top Gun
my_movie = media.Movie(
        "Top Gun",
        "Top naval pilot school",
        "https://goo.gl/iH2mwW",
        "https://www.youtube.com/watch?v=qAfbp3YX9F0")

# and School of Rock
school_of_rock = media.Movie(
        "School of Rock",
        "Storyline",
        "https://goo.gl/N55NKQ",
        "https://www.youtube.com/watch?v=3PsUJFEBC74")

# and Ratatouille
ratatouille = media.Movie(
        "Ratatouille",
        "Storyline",
        "https://goo.gl/wPtp6F",
        "https://www.youtube.com/watch?v=c3sBBRxDAqk")

# and Midnight in Paris
midnight_in_paris = media.Movie(
        "Midnight in Paris",
        "Storyline",
        "https://goo.gl/YjgLbV",
        "https://www.youtube.com/watch?v=atLg2wQQxvU")

# and Hunger Games
hunger_games = media.Movie(
        "Hunger Games",
        "Storyline",
        "http://upload.wikimedia.org/wikipedia/en/4/42/HungerGamesPoster.jpg",
        "https://www.youtube.com/watch?v=PbA63a7H0bo")

# create list of all movies to feed to the web page generator
movies = [toy_story,
          avatar,
          school_of_rock,
          ratatouille,
          midnight_in_paris,
          hunger_games]

# generate webpage and display it
fresh_tomatoes.open_movies_page(movies)
