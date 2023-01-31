from ForumProject.src.FilePost import FilePost
from ForumProject.src.Post import Post
from ForumProject.src.Thread import Thread


class User:
    """Utilisateur."""

    def __init__(self, username, password):
        """Initialise le nom d'utilisateur et le mot de passe."""
        self.username = username
        self.password = password

    def login(self):
        """Connecte l'utilisateur."""
        print(f"L'utilisateur {self.username} est connecté.")

    def post(self, thread, content, file=None):
        """Poste un message dans un fil de discussion."""
        if file:
            post = FilePost(self, "aujourd'hui", content, file)
        else:
            post = Post(user=self, time_posted="aujourd'hui", content=content)
        thread.add_post(post)
        return post

    def make_thread(self, title, content):
        """Créé un nouveau fil de discussion."""
        post = Post(self, "aujourd'hui", content)
        return Thread(title, "aujourd'hui", post)

    def __str__(self):
        """représentation de l'utilisateur."""
        return self.username
