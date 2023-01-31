from ForumProject.src.ImageFile import ImageFile


class GifImageFile(ImageFile):
    """Fichier image Gif."""

    def display(self):
        """Affiche l'image."""
        super().display()
        print("L'image est de type 'GIF'.")
