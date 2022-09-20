from project.movie_specification.movie import Movie
from project.user import User


class MovieApp:
    def __init__(self):
        self.movie_collection = []
        self.users_collection = []

    def register_user(self, username, age):
        pass

    def upload_movie(self, username, movie: Movie):
        pass

    def edit_movie(self, username, movie: Movie, **kwargs):
        pass

    def delete_movie(self, username, movie: Movie):
        pass

    def like_movie(self, username, movie: Movie):
        pass

    def dislike_movie(self, username, movie: Movie):
        pass

    def display_movies(self):
        pass

    def __str__(self):
        pass
