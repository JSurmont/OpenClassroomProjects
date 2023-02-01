from MovieLibraryProject.film.movie import MovieAbstract


class Friend:

    def __init__(self, name: str, movie: MovieAbstract = None):
        self.name = name
        self.movie = movie

        if movie:
            movie.lieu = self

    def __str__(self) -> str:
        return f"{self.name}"

    def __repr__(self) -> str:
        return self.__str__()
