class Thread:
    """Fil de discussions."""

    def __init__(self, title, time_posted, post):
        """Initialise le titre, la date et les posts.
        Attention ici: on commence par un seul post, celui du sujet.
        Les réponses à ce post ne pourrons s'ajouter qu'ultérieurement.
        En effet, on ne créé pas directement un nouveau fil avec des réponses. ;)
        """
        self.title = title
        self.time_posted = time_posted
        self.posts = [post]

    def display(self):
        """Affiche le fil de discussion."""
        print("----- THREAD -----")
        print(f"titre: {self.title}, date: {self.time_posted}")
        print()
        for post in self.posts:
            post.display()
            print()
        print("------------------")

    def add_post(self, post):
        """Ajoute un post."""
        self.posts.append(post)
