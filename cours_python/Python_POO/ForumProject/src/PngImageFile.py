from ForumProject.src.ImageFile import ImageFile


class PngImageFile(ImageFile):
    """Fichier image PNG."""

    def display(self):
        """Affiche l'image."""
        super().display()
        print("L'image est de type 'PNG'.")
