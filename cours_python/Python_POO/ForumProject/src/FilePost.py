from ForumProject.src.Post import Post


class FilePost(Post):
    """Message comportant un fichier."""

    def __init__(self, user, time_posted, content, file):
        """Initialise le fichier."""
        super().__init__(user, time_posted, content)
        self.file = file

    def display(self):
        """Affiche le contenu et le fichier."""
        super().display()
        print("pièce jointe:")
        self.file.display()
