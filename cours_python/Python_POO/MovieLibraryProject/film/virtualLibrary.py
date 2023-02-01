import random

from MovieLibraryProject.film.movie import MovieAbstract
from MovieLibraryProject.film.movieCleaner import MovieCleaner
from MovieLibraryProject.film.data import films


class VirtualLibrary:

    def __init__(self):
        """Initialise les films."""
        self.movies = []

        for film_data in films:
            film: MovieAbstract = MovieCleaner(film_data).generate()
            film.lieu = self
            self.movies.append(film)

        self.sort_by_date_and_name()

    def sort_by_date_and_name(self):
        """Tri les films par date et par nom."""
        self.movies.sort(key=lambda film: (film.date, film.name))

    def sort_by_type(self):
        """Tri les films par type."""
        self.movies.sort(key=lambda film: film.type)

    def get_random_choice(self) -> MovieAbstract:
        """Retourne un film au hasard."""
        return random.choice(self.movies)

    def get_films_lent(self) -> [MovieAbstract]:
        """retourne la liste des films prêtés.
        Note: On pourrait aussi utiliser une liste de compréhension ici.
        """
        films_lent = []

        for film in self.movies:
            if film.lieu is not self:  # le film n'est pas dans la bibliothèque
                films_lent.append(film)

        return films_lent

    def get_film_borrower(self, film: MovieAbstract):
        if film.lieu is self:
            return None

        return film.lieu

    def find_by_name(self, name):
        """Retourne un film si le nom correspond, sinon None."""
        for film in self.movies:
            if name == film.name:
                return film
        return None
