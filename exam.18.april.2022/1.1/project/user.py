class User:
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
        if len(value) == 0:
            raise ValueError("Invalid username!")
        self.__username = value

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        if value < 6:
            raise ValueError("Users under the age of 6 are not allowed!")
        self.__age = value

    @staticmethod
    def return_details(movies_status):
        result = ''
        for movie in movies_status:
            movie_details = movie.details()
            result = movie_details + '\n'
        return result

    def add_owned_movie(self, movie):
        self.movies_owned.append(movie)

    def remove_owned_movie(self, given_movie):
        for idx, movie in enumerate(self.movies_owned):
            if movie == given_movie:
                self.movies_owned.pop(idx)
                return

    def add_liked_movie(self, movie):
        self.movies_liked.append(movie)

    def remove_liked_movie(self, given_movie):
        for idx, movie in enumerate(self.movies_liked):
            if movie == given_movie:
                self.movies_liked.pop(idx)
                return

    def liked_movies_titles(self):
        return [x.title for x in self.movies_liked]

    def __str__(self):
        output = f"Username: {self.username}, Age: {self.age}\nLiked movies:\n"

        if self.movies_liked:
            output += self.return_details(self.movies_liked)
        else:
            output += 'No movies liked.\n'

        if self.movies_owned:
            output += self.return_details(self.movies_owned)
        else:
            output += 'No movies owned.\n'

        return output.strip()
