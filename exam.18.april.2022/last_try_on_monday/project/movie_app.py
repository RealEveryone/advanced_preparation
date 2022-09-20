from project.movie_specification.movie import Movie
from project.user import User


class MovieApp:
    def __init__(self):
        self.movies_collection = []
        self.users_collection = []
        self.users_as_dict = {}

    def register_user(self, username, age):
        self.__check_if_user_exist(username)
        user = User(username, age)
        self.users_collection.append(user)
        self.users_as_dict[username] = user
        return f"{username} registered successfully."

    def upload_movie(self, username: str, movie: Movie):
        self.__check_if_user_does_not_exist(username)
        self.__check_if_user_is_movie_owner(username, movie)
        self.__check_if_movie_is_uploaded(movie)
        self.append_movie(self.users_as_dict[username], movie)
        return f"{username} successfully added {movie.title} movie."

    def edit_movie(self, username: str, movie: Movie, **kwargs):
        self.__check_if_movie_does_not_exist(movie)
        self.__check_if_user_is_movie_owner(username, movie)

        for attr, value in kwargs.items():
            setattr(movie, attr, value)
        return f"{username} successfully edited {movie.title} movie."

    def delete_movie(self, username: str, movie: Movie):
        self.__check_if_movie_does_not_exist(movie)
        self.__check_if_user_is_movie_owner(username, movie)
        self.remove_movie(self.users_as_dict[username], movie)
        return f"{username} successfully deleted {movie.title} movie."

    def like_movie(self, username: str, movie: Movie):
        self.__check_if_user_is_not_movie_owner(username, movie)
        self.__check_if_user_already_liked_movie(self.users_as_dict[username], movie)
        movie.like()
        self.users_as_dict[username].movies_liked.append(movie)
        return f"{username} liked {movie.title} movie."

    def dislike_movie(self, username, movie):
        if movie not in self.users_as_dict[username].movies_liked:
            raise Exception(f"{username} has not liked the movie {movie.title}!")
        self.users_as_dict[username].movies_liked.remove(movie)
        return f"{username} disliked {movie.title} movie."

    def display_movies(self):
        output = ''
        if self.movies_collection:
            for movie in sorted(self.movies_collection, key=lambda x: (-x.year, x.title)):
                output += movie.details() + '\n'
        else:
            output = "No movies found.\n"
        return output.strip()

    def __str__(self):
        output = 'All users: '
        users = 'No users.'
        if self.users_collection:
            users = ', '.join([x.username for x in self.users_collection])
        output += users + '\n'
        output += 'All movies: '
        movies = 'No movies.'
        if self.movies_collection:
            movies = ', '.join([x.title for x in self.movies_collection])
        output += movies
        return output

    def __check_if_user_exist(self, username):
        if username in [u.username for u in self.users_collection]:
            raise Exception("User already exists!")

    def __check_if_user_does_not_exist(self, username):
        if username not in [u.username for u in self.users_collection]:
            raise Exception("This user does not exist!")

    def __check_if_movie_does_not_exist(self, movie):
        if movie not in self.movies_collection:
            raise Exception(f"The movie {movie.title} is not uploaded!")

    def __check_if_movie_is_uploaded(self, movie):
        if movie in self.movies_collection:
            raise Exception("Movie already added to the collection!")

    @staticmethod
    def __check_if_user_already_liked_movie(user, movie):
        if movie in user.movies_liked:
            raise Exception(f"{user.username} already liked the movie {movie.title}!")

    def append_movie(self, user, movie):
        user.movies_owned.append(movie)
        self.movies_collection.append(movie)

    def remove_movie(self, user, movie):
        user.movies_owned.remove(movie)
        self.movies_collection.remove(movie)

    @staticmethod
    def __check_if_user_is_movie_owner(user, movie):
        if user != movie.owner.username:
            raise Exception(f"{user} is not the owner of the movie {movie.title}!")

    @staticmethod
    def __check_if_user_is_not_movie_owner(user, movie):
        if user == movie.owner.username:
            raise Exception(f"{user} is the owner of the movie {movie.title}!")
