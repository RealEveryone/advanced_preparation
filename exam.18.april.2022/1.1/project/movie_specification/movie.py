from abc import ABC, abstractmethod

from project.user import User


class Movie(ABC):
    AGE_RESTRICTION = 0

    def __init__(self, title, year, owner, age_restriction):
        self.title = title
        self.year = year
        self.owner = owner
        self.age_restriction = age_restriction
        self.likes = 0

    def like_movie(self):
        self.likes += 1

    def unlike_movie(self):
        self.likes -= 1

    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self, value):
        if len(value) == 0:
            raise ValueError("The title cannot be empty string!")
        self.__title = value

    @property
    def year(self):
        return self.__year

    @year.setter
    def year(self, value):
        if value < 1888:
            raise ValueError("Movies weren't made before 1888!")
        self.__year = value

    @property
    def owner(self):
        return self.__owner

    @owner.setter
    def owner(self, value):
        if not isinstance(value, User):
            raise ValueError("The owner must be an object of type User!")
        self.__owner = value

    @property
    def age_restriction(self):
        return self.__age_restriction

    @age_restriction.setter
    def age_restriction(self, value):
        if value < self.AGE_RESTRICTION:
            raise ValueError(f"{self.__class__.__name__} movies must be restricted for "
                             f"audience under {self.AGE_RESTRICTION} years!")
        self.__age_restriction = value

    @abstractmethod
    def details(self):
        pass
