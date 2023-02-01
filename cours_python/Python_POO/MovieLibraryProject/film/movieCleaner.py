from MovieLibraryProject.film.dvdMovie import DvdMovie
from MovieLibraryProject.film.movie import MovieAbstract
from MovieLibraryProject.film.vhfMovie import VhfMovie


class MovieCleaner:
    """Génère un film à partir de données brutes."""

    NAME_AND_DATE_INDEX = 0
    TYPE_INDEX = 1

    def __init__(self, film_data):
        self.film_data = film_data

    def generate(self) -> MovieAbstract:
        """Génère le film."""
        name: str = self.generate_name()
        date: int = self.generate_date()
        movie_type: str = self.generate_type()

        # ici on itère sur un tuple de classes (et non d'instances) !
        for Film in (VhfMovie, DvdMovie):
            # on vérifie le type du film par rapport au type de chaque classe
            if movie_type == Film.type:
                # et on retourne un instance de la classe choisie.
                return Film(name, date)

    def generate_name(self) -> str:
        """Génère le nom."""
        name_date = self.film_data[self.NAME_AND_DATE_INDEX]
        return name_date[: name_date.index("(")].strip()

    def generate_date(self) -> int:
        """Génère la date."""
        name_date = self.film_data[self.NAME_AND_DATE_INDEX]
        date_with_parenthesis = name_date[name_date.index("("):]
        date_letters = date_with_parenthesis.replace("(", "").replace(")", "")
        return int(date_letters)

    def generate_type(self) -> str:
        """Génère le type."""
        return self.film_data[self.TYPE_INDEX].lower()
