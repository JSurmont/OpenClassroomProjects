"""Point d'entrée."""

from Contact.user import User
from Contact.owlcontact import OwlContactSystem
from Contact.textcontact import TextContactSystem
from Contact.helpers import send_mass_messages


def main():
    """Main function."""
    alice = User("Alice", TextContactSystem("0102030405"))
    bob = User("Bob", OwlContactSystem("4 Privet Drive"))

    user_list = [alice, bob]
    send_mass_messages("Hello {name}, Comment vas-tu?", user_list)
    send_mass_messages(
        "Salut {name}. Tes informations de Contact sont-elles corrects?"
        " Nous avons celles-ci: {contact_info}.",
        user_list,
    )


if __name__ == "__main__":
    main()
