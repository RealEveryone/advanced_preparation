from abc import ABC, abstractmethod

from project.user import User


class Movie(ABC):
    OLDEST_MOVIE_RELEASE = 1888
    MINIMAL_AGE_RESTRICTION = 6

    def __init__(self, title, year, owner, age_restriction):
        self.title = title
        self.year = year
        self.owner = owner
        self.age_restriction = age_restriction
        self.likes = 0

    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self, value):
        self.__validate_title(value)
        self.__title = value

    @property
    def year(self):
        return self.__year

    @year.setter
    def year(self, value):
        self.__validate_year(value)
        self.__year = value

    @property
    def owner(self):
        return self.__owner

    @owner.setter
    def owner(self, value):
        self.__validate_owner(value)
        self.__owner = value

    @property
    def age_restriction(self):
        return self.__age_restriction

    @age_restriction.setter
    def age_restriction(self, value):
        self.__validate_age_restriction(value)
        self.__age_restriction = value

    @property
    @abstractmethod
    def type(self):
        pass

    @staticmethod
    def __validate_title(title):
        if not isinstance(title, str) or len(title) == 0:
            raise ValueError("The title cannot be empty string!")

    @classmethod
    def __validate_year(cls, year):
        if year < cls.OLDEST_MOVIE_RELEASE:
            raise ValueError(f"Movies weren't made before {cls.OLDEST_MOVIE_RELEASE}!")

    @staticmethod
    def __validate_owner(owner):
        if not isinstance(owner, User):
            raise ValueError("The owner must be an object of type User!")

    def __validate_age_restriction(self, age):
        if age < self.MINIMAL_AGE_RESTRICTION:
            raise ValueError(f"{self.type} movies must be restricted for audience under "
                             f"{self.MINIMAL_AGE_RESTRICTION} years!")

    def like(self):
        self.likes += 1

    def dislike(self):
        self.likes -= 1

    def details(self):
        return f"{self.type} - Title:{self.title},"              \
               f" Year:{self.year},"                        \
               f" Age restriction:{self.age_restriction},"  \
               f" Likes:{self.likes},"                      \
               f" Owned by:{self.owner.username}"

