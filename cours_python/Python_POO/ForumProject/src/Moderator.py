from ForumProject.src.User import User


class Moderator(User):
    """Utilisateur modérateur."""

    def edit(self, post, content):
        """Modifie un message."""
        post.content = content

    def delete(self, thread, post):
        """Supprime un message."""
        index = thread.posts.index(post)
        del thread.posts[index]
