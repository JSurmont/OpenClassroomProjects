import random
import os
import textwrap
from PIL import Image, ImageFont, ImageDraw


from fbapp.models import Content, Gender


def find_random_content_by_gender(gender):
    contents = Content.query.filter(Content.gender == Gender[gender]).all()
    return random.choice(contents)


class OpenGraphImage:

    def __init__(self, uid, first_name: str, text: str):
        self.location = self._location(uid)

        background = self.base()

        self.print_on_image(background, first_name.capitalize(), 70, 50)

        # textwrap découpe une chaine de caractères sans couper les mots au milieu.
        sentences = textwrap.wrap(text, width=60)

        # current_h : Hauteur à laquelle commencer à écrire
        # pad : pixels à ajouter entre chaque ligne, en hauteur.
        current_h, pad = 180, 10

        for sentence in sentences:
            w, h = self.print_on_image(background, sentence, 40, current_h)

            # on incrémente la hauteur pour créer une nouvelle ligne en-dessous.
            current_h += h + pad

        background.show()

    def base(self):
        img = Image.new('RGB', (1200, 630), '#18BC9C')
        return img

    def print_on_image(self, img, text, size, height):
        # On commence par charger la police utilisée.
        font = ImageFont.truetype(os.path.join('fbapp', 'static', 'fonts', 'Arcon-Regular.otf'), size)

        # Création d'une nouvelle instance
        draw = ImageDraw.Draw(img)

        # textsize renvoie la largeur et la hauteur en pixel d'une chaine de caractères donnée.
        w = draw.textlength(text, font)
        h = size

        # Calcul de la position pour que le texte soit centré et non pas aligné à gauche.
        position = ((img.width - w) / 2, height)

        # Ajout du texte à l'image.
        draw.text(position, text, (255, 255, 255), font=font)

        return w, h

    def _location(self, uid):
        return 'tmp/{}.jpg'.format(uid)

    def _path(self, uid):
        # Le nom de l'image est l'identifiant Facebook de la personne. Cela nous garantit de ne pas avoir de doublon.
        return os.path.join('fbapp', 'static', 'tmp', '{}.jpg'.format(uid))
