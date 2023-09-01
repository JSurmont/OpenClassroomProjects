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
        to='self',
        through='Follow',
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


# https://adamj.eu/tech/2021/02/26/django-check-constraints-prevent-self-following/
class Follow(models.Model):
    from_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="+")
    to_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="+")

    class Meta:
        constraints = [
            models.UniqueConstraint(
                name="%(app_label)s_%(class)s_unique_relationships",
                fields=["from_user", "to_user"],
            ),
            models.CheckConstraint(
                name="%(app_label)s_%(class)s_prevent_self_follow",
                check=~models.Q(from_user=models.F("to_user")),
            ),
        ]
