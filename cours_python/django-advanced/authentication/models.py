from django.db import models
from django.contrib.auth.models import AbstractUser, Group


class User(AbstractUser):

    CREATOR = 'CREATOR'
    SUBSRIBER = 'SUBSCRIBER'

    ROLE_CHOICES = (
        (CREATOR, 'Créateur'),
        (SUBSRIBER, 'Abonné')
    )

    profile_photo = models.ImageField(verbose_name='Photo de profil')
    role = models.CharField(max_length=30, choices=ROLE_CHOICES, verbose_name='Rôle')
    follows = models.ManyToManyField(
        'self',
        limit_choices_to={'role': CREATOR},
        symmetrical=False,
        verbose_name='suit',
    )

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if self.role == self.CREATOR:
            group = Group.objects.get(name='creators')
            group.user_set.add(self)
        if self.role == self.SUBSRIBER:
            group = Group.objects.get(name='subscribers')
            group.user_set.add(self)
