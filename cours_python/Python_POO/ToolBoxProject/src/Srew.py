class Screw:
    """Vis."""

    MAX_TIGHTNESS = 5

    def __init__(self):
        """Initialise son degré de serrage."""
        self.tightness = 0

    def tighten(self):
        """Serre le vis."""
        if self.tightness < self.MAX_TIGHTNESS:
            self.tightness += 1

    def loosen(self):
        """Déserre le vis."""
        if self.tightness > 0:
            self.tightness -= 1

    def __str__(self):
        """Retourne une forme lisible de l'objet."""
        return "Vis avec un serrage de {}".format(self.tightness)
