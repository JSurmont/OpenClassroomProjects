# Generated by Django 3.2.5 on 2021-07-03 07:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('favourites', '0002_favouriteproduct_is_favoutire'),
    ]

    operations = [
        migrations.AlterField(
            model_name='favouriteproduct',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user', to=settings.AUTH_USER_MODEL),
        ),
    ]
