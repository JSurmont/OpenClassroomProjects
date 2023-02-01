from pprint import pprint

from MovieLibraryProject.film.friendsCleaner import FriendCleaner
from MovieLibraryProject.film.virtualLibrary import VirtualLibrary


def main():
    """Code client."""
    library = VirtualLibrary()

    films = library.movies
    friends = FriendCleaner().list_from_data(library)

    print("Tous mes films:")
    pprint(films)
    print()
    print("Tous mes amis:")
    pprint(friends)
    print()

    library.sort_by_type()
    print("Mes films triés par type:")
    pprint(films)
    print()

    film = library.get_random_choice()
    print(f"Film récupéré au hasard: {film}")
    print()

    films_lent = library.get_films_lent()
    print("J'ai prêté ces films:")
    pprint(films_lent)
    print()

    for film in films_lent:
        print(f"Le film '{film}' est chez", film.lieu)


if __name__ == '__main__':
    main()
