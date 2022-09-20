from project.movie_specification.movie import Movie
from project.user import User


class MovieApp:
    def __init__(self):
        self.movies_collection = []
        self.users_collection = []

    def __find_user_by_name(self, username):
        for user in self.users_collection:
            if user.username == username:
                return user
        return None

    def __find_movie_by_title(self, title):
        for movie in self.movies_collection:
            if movie.title == title:
                return movie
        return None

    def __remove_movie_from_everywhere(self, given_movie, user):
        user.remove_owned_movie(given_movie)
        for idx, movie in enumerate(self.movies_collection):
            if given_movie == movie:
                self.movies_collection.pop(idx)
                return

    def register_user(self, username, age):
        if self.__find_user_by_name(username):
            raise Exception("User already exists!")
        user = User(username, age)
        self.users_collection.append(user)
        return f"{username} registered successfully."

    def upload_movie(self, username, movie: Movie):
        user = self.__find_user_by_name(username)

        if user is None:
            raise Exception("This user does not exist!")
        if self.__find_movie_by_title(movie.title):
            raise Exception("Movie already added to the collection!")
        if movie.owner != user:
            raise Exception(F"{username} is not the owner of the movie {movie.title}!")

        user.add_owned_movie(movie)
        self.movies_collection.append(movie)
        return f"{username} successfully added {movie.title} movie."

    def edit_movie(self, username, movie: Movie, **kwargs):
        if self.__find_movie_by_title(movie.title) is None:
            raise Exception(f"The movie {movie.title} is not uploaded!")
        user = self.__find_user_by_name(username)
        if movie.owner != user:
            raise Exception(f"{username} is not the owner of the movie {movie.title}!")
        for attr, value in kwargs.items():
            setattr(movie, attr, value)
        return f"{username} successfully edited {movie.title} movie."

    def delete_movie(self, username, movie: Movie):
        if self.__find_movie_by_title(movie.title) is None:
            raise Exception(f"The movie {movie.title} is not uploaded!")
        user = self.__find_user_by_name(username)
        if movie.owner != user:
            raise Exception(f"{username} is not the owner of the movie {movie.title}!")
        self.__remove_movie_from_everywhere(movie, user)
        return f"{username} successfully deleted {movie.title} movie."

    def like_movie(self, username, movie: Movie):
        user = self.__find_user_by_name(username)
        if user.username == movie.owner.username:
            raise Exception(f"{username} is the owner of the movie {movie.title}!")
        if movie.title in user.liked_movies_titles():
            raise Exception(f"{username} already liked the movie {movie.title}!")
        movie.like_movie()
        user.add_liked_movie(movie)
        return f"{username} liked {movie.title} movie."

    def dislike_movie(self, username, movie: Movie):
        user = self.__find_user_by_name(username)
        if movie not in user.liked_movies_titles():
            raise Exception(f"{username} has not liked the movie {movie.title}!")
        user.remove_liked_movie(movie)
        movie.unlike_movie()
        return f"{username} disliked {movie.title} movie."

    def display_movies(self):
        result = []
        if self.movies_collection:
            for movies in sorted(self.movies_collection, key=lambda x: (-x.year, x.title)):
                movie_details = movies.details()
                result.append(movie_details)
            return '\n'.join(result)
        return 'No movies found.'

    def __str__(self):
        output = 'All users: '
        if self.users_collection:
            result = []
            for user in self.users_collection:
                user_details = user.username
                result.append(user_details)
            output += ', '.join(result)
        else:
            output += 'No users.'

        output += '\nAll movies: '

        if self.movies_collection:
            result = []
            for movie in self.movies_collection:
                movie_details = movie.title
                result.append(movie_details)
            output += ', '.join(result)
        else:
            output += 'No movies.'

        return output
