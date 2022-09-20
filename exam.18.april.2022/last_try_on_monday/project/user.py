import os


class User:
    MIN_USER_AGE = 6

    def __init__(self, username, age):
        self.username = username
        self.age = age
        self.movies_liked = []
        self.movies_owned = []

    @property
    def username(self):
        return self.__username

    @username.setter
    def username(self, value):
        self.__validate_username(value)
        self.__username = value

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        if value < self.MIN_USER_AGE:
            raise ValueError(f"Users under the age of {self.MIN_USER_AGE} are not allowed!")
        self.__age = value

    @staticmethod
    def __validate_username(name):
        if not isinstance(name, str) or len(name) == 0:
            raise ValueError("Invalid username!")

    def __str__(self):
        liked_movies = "No movies liked."
        if self.movies_liked:
            liked_movies = os.linesep.join([movie.details() for movie in self.movies_liked])
        owned_movies = "No movies owned."
        if self.movies_owned:
            owned_movies = os.linesep.join([movie.details() for movie in self.movies_owned])
        return f'''Username: {self.username}, Age: {self.age}
Liked movies:
{liked_movies}
Owned movies:
{owned_movies}'''
