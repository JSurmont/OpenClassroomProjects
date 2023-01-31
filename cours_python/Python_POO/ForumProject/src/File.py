from abc import ABC


class File(ABC):
    """Fichier."""

    def __init__(self, name, size):
        """Initialise le nom et la taille."""
        self.name = name
        self.size = size

    def display(self):
        """Affiche le fichier."""
        print(f"Fichier '{self.name}'.")
