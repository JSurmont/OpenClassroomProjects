from MovieLibraryProject.film.movie import MovieAbstract


class VhfMovie(MovieAbstract):
    type = "vhf"

    def __init__(self, name: str, date: int, lieu=None):
        """Initialise le type."""
        super().__init__(name, date, lieu)
        self.magnetic_tape = True
