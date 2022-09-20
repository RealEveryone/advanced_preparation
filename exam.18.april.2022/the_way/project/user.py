import os


class User:
    USER_MIN_AGE = 6

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
        self.__validate_age(value)
        self.__age = value

    def __str__(self):
        liked_movies = "No movies liked."
        owned_movies = "No movies owned."
        if self.movies_liked:
            liked_movies = os.linesep.join([m.details() for m in self.movies_liked])
        if self.movies_owned:
            owned_movies = os.linesep.join([m.details() for m in self.movies_owned])
        output = f"Username: {self.username}, Age: {self.age}\n" \
                 f"Liked movies:  \n" \
                 f"{liked_movies} \n" \
                 f"Owned movies:  \n" \
                 f"{owned_movies} \n"
        return output.strip()

    @staticmethod
    def __validate_username(username):
        if not isinstance(username, str) or len(username) == 0:
            raise ValueError("Invalid username!")

    def __validate_age(self, age):
        if age < self.USER_MIN_AGE:
            raise f"Users under the age of {self.USER_MIN_AGE} are not allowed!"
