from ForumProject.src.File import File


class ImageFile(File):
    """Fichier image."""

    def display(self):
        """Affiche l'image."""
        print(f"Fichier image '{self.name}'.")
