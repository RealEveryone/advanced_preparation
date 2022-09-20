from project.movie_specification.movie import Movie
from project.user import User


class MovieApp:
    def __init__(self):
        self.movies_collection = []
        self.users_collection = []

    def __movie_exists(self, title):
        for movie in self.movies_collection:
            if movie.title == title:
                return True
        return False

    def register_user(self, username, age):
        for user in self.users_collection:
            if user.username == username:
                return f'User already exists!'
        current_user = User(username, age)
        self.users_collection.append(current_user)
        return f'{username} registered successfully.'

    def upload_movie(self, username, movie: Movie):
        usernames_list = [i.username for i in self.users_collection]
        if username not in usernames_list:
            raise Exception('This user does not exists!')
        if self.__movie_exists(movie.title):
            raise Exception('Movie already added to the collection!')
        if username != movie.owner.username:
            raise Exception(f'{username} is not the owner of the movie {movie.title}!')

        for user in self.users_collection:
            if user.username == username:
                user.movies_owned.append(movie)
        self.movies_collection.append(movie)
        return f'{username} successfully added {movie.title} movie.'

    def edit_movie(self, username, movie: Movie, **kwargs):
        if not self.__movie_exists(movie.title):
            raise Exception(f'The movie {movie.title} is not uploaded!')
        if username != movie.owner.username:
            raise Exception(f'{username} is not the owner of the movie {movie.title}!')
        output = ''
        for key, value in kwargs.items():
            setattr(movie, key, value)
        output += f'{username} successfully edited {movie.title} movie.'
        return output.strip()

    def delete_movie(self, username, movie: Movie):
        if not self.__movie_exists(movie.title):
            raise Exception(f'The movie {movie.title} is not uploaded!')
        if username != movie.owner.username:
            raise Exception(f"{username} is not owner of the movie {movie.title}!")

        for user in self.users_collection:
            if user.username == username:
                user.movies_owned.pop(user.movies_owned.index(movie))
        self.movies_collection.pop(self.movies_collection.index(movie))
        return f'{username} successfully deleted {movie.title} movie.'

    def like_movie(self, username, movie: Movie):
        if username == movie.owner.username:
            raise Exception(f'{username} is the owner of the movie {movie.title}')
        for user in self.users_collection:
            if username == user.username:
                if movie in user.movies_liked:
                    raise Exception(f'{username} already liked the movie {movie.title}')
                user.movies_liked.append(movie)
                movie.likes += 1
        return f'{username} liked {movie.title} movie.'

    def dislike_movie(self, username, movie: Movie):
        for user in self.users_collection:
            if user.username == username:
                if movie in user.movies_liked:
                    movie.likes -= 1
                    user.movies_liked.remove(movie)
                    return f'{username} disliked {movie.title} movie.'
            raise Exception(f'{username} has not liked the movie {movie.title}!')

    def display_movies(self):
        if not self.movies_collection:
            return 'No movies found.'
        output = ''
        for movie in sorted(self.movies_collection, key=lambda x: (-x.year, x.title)):
            output += movie.details() + '\n'
        return output.strip()

    def __str__(self):

        output = 'All users: '
        if self.users_collection:
            output += ', '.join([i.username for i in self.users_collection]) + '\n'
        else:
            output += 'No Users' + '\n'
        output += 'All movies: '
        if self.movies_collection:
            output += ', '.join([i.title for i in self.movies_collection])
        else:
            output += 'No movies.'

        return output
