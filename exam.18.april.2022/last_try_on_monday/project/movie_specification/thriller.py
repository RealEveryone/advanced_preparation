from project.movie_specification.movie import Movie


class Thriller(Movie):
    MINIMAL_AGE_RESTRICTION = 16

    def __init__(self, title, year, owner, age_restriction=None):
        super().__init__(title, year, owner,
                         age_restriction if age_restriction else self.MINIMAL_AGE_RESTRICTION)

    @property
    def type(self):
        return 'Thriller'
