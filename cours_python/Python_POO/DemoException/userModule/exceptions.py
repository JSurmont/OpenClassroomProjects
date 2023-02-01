class UsernameTooShortException(Exception):
    """Erreur sur le nom d'utilisateur."""

    def __init__(self, msg="", *args, **kwargs):
        """Init le message."""
        msg = msg or "Le nom d'utilisateur est trop court !"
        super().__init__(msg, *args, **kwargs)
        

class PasswordTooShortException(Exception):
    """Erreur sur le mot de passe."""

    def __init__(self, msg="", *args, **kwargs):
        """Init le message."""
        msg = msg or "Le mot de passe est trop court !"
        super().__init__(msg, *args, **kwargs)
