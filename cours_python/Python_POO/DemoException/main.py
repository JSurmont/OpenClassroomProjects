from DemoException.userModule.exception import UsernameTooShortException
from DemoException.userModule.exception import PasswordTooShortException
from DemoException.userModule.user import user


if __name__ == "__main__":
    user = User("John", "supersecret")
    try:
        user = User("t", "supersecret")
    except UsernameTooShortException:
        print("L'exception sur le nom d'utilisateur a été levée.")

    try:
        user = User("John", "t")
    except PasswordTooShortException:
        print("L'exception sur le mot de passe a été levée.")
