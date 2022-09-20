class User:
    def __init__(self, username: str, age: int):
        self.username = username
        self.age = age
        self.movies_liked = []
        self.movies_owned = []

    @property
    def username(self):
        return self.__username

    @username.setter
    def username(self, value):
        if value is None:
            raise ValueError('Invalid username!')
        self.__username = value

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        if value < 6:
            raise ValueError('User under the age of 6 are not allowed!')
        self.__age = value

    def __str__(self):
        output = f'Username: {self.username}, Age: {self.age}\n' + 'Liked movies:\n'

        if self.movies_liked:
            for current_movie in self.movies_liked:
                output += current_movie.details() + '\n'
        else:
            output += 'No movies liked.'

        if self.movies_owned:
            for current_movie in self.movies_owned:
                output += current_movie.details() + '\n'
        else:
            output += 'No movies owned.'

        return output.strip()

