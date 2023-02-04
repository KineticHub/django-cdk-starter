# Generated by Django 4.0.8 on 2023-02-04 17:37

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('house', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='house',
            name='family_guests',
            field=models.ManyToManyField(null=True, related_name='guest_houses', to=settings.AUTH_USER_MODEL),
        ),
    ]