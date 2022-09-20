from project.movie_specification.movie import Movie


class Fantasy(Movie):
    def __init__(self, title, year, owner, age_restriction=None):
        super().__init__(title, year, owner,
                         age_restriction if age_restriction else self.MINIMAL_AGE_RESTRICTION)
    @property
    def type(self):
        return 'Fantasy'
