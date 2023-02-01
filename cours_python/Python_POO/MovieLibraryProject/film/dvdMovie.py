from MovieLibraryProject.film.movie import MovieAbstract


class DvdMovie(MovieAbstract):
    type = "dvd"

    def __init__(self, name: str, date: int, lieu=None):
        """Initialise le type."""
        super().__init__(name, date, lieu)
        self.mega_octets = 4700
