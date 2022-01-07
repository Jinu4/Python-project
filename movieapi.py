import omdbapi
from omdbapi.movie_search import GetMovie
m = GetMovie(api_key='23ffcbc6')
m.get_movie(title='Hello')
