class ScrewDriver:
    """Tournevis."""

    def __init__(self, size=3):
        """Initialise la taille."""
        self.size = size

    def tighten(self, screw):
        """Serrer une vis."""
        screw.tighten()

    def loosen(self, screw):
        """Desserre une vis."""
        screw.loosen()

    def __repr__(self):
        """Représentation de l'objet."""
        return f"Tournevis de taille {self.size}"
