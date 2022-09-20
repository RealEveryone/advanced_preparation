from project.movie_specification.fantasy import Fantasy
from project.user import User

user1 = User('Name', 13)
movie1 = Fantasy('Movie', 2021, user1, 7)
user1.movies_liked.append(movie1)
user1.movies_liked.append(movie1)
user1.movies_liked.append(movie1)
print(str(user1))