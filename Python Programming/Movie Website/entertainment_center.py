import media, fresh_tomatoes

toy_story = media.Movie(
    "Toy Story", 
    "A story of his boy and his toys that come to life",
    "https://duckduckgo.com/i/4c821060.jpg", 
    "https://www.youtube.com/watch?v=wmiIUN-7qhE")

avatar = media.Movie(
    "Avatar", 
    "A marine gets rekt on an alien planet I'm pretty sure",
    "https://proxy.duckduckgo.com/iu/?u=https%3A%2F%2Ftse1.mm.bing.net%2Fth%3Fid%3DOIP.poW-Slzp6GyAE8gJvzwVwwHaKj%26pid%3DApi&f=1",
    "https://www.youtube.com/watch?v=6ziBFh3V1aM",
)

star_wars = media.Movie(
    "Star Wars",
    "A bunch of wild stuff happens",
    "https://proxy.duckduckgo.com/iu/?u=http%3A%2F%2F4.bp.blogspot.com%2F-ygq1lvk2HUA%2FUNShFBvZoRI%2FAAAAAAAAAGg%2FhxHVeirpXfw%2Fs1600%2Fessence-of-star-wars.jpg&f=1",
    "https://www.youtube.com/watch?v=y6120QOlsfU",
)

movies = [star_wars, toy_story, avatar]

fresh_tomatoes.open_movies_page(movies)
