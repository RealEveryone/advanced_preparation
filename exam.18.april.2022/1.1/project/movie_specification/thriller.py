from project.movie_specification.movie import Movie


class Action(Movie):
    AGE_RESTRICTION = 16

    def __init__(self, title, year, owner, age_restriction=AGE_RESTRICTION):
        super().__init__(title, year, owner, age_restriction)

    def details(self):
        return f"Thriller - Title:{self.title}, Year:{self.year}, Age restriction:{self.age_restriction}, " \
               f"Likes:{self.likes}, Owned by:{self.owner.name}"
