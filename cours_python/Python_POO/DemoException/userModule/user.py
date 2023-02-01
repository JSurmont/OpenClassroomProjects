from DemoException.userModule.exception import UsernameTooShortException
from DemoException.userModule.exception import PasswordTooShortException


class User:
    """Un utilisateur."""

    def __init__(self, username, password):
        """Initialise le nom et le mot de passe."""
        if len(username) < 2:
            raise UsernameTooShortException()
        if len(password) < 10:
            raise PasswordTooShortException()

        self.username = username
        self.password = password
