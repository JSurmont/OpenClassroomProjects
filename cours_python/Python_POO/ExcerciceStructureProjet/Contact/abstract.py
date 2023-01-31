"""Définit la classe de Contact abstraite."""

from abc import ABC, abstractmethod


class ContactSystem(ABC):
    """Classe abstraite utilisée pour envoyer un message à un utilisateur."""

    @abstractmethod
    def send(self, message):
        """Toutes les sous-classes de COntactSystem doivent implémenter send."""
        pass
