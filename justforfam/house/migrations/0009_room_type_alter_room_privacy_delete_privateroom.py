# Generated by Django 4.0.8 on 2023-02-12 17:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('house', '0008_remove_house_family_guests_house_neighbours'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='type',
            field=models.CharField(choices=[('living-room', 'Living Room'), ('family-den', 'Family Den'), ('bedroom', 'Bedroom')], default='living-room', max_length=255),
        ),
        migrations.AlterField(
            model_name='room',
            name='privacy',
            field=models.CharField(choices=[('private', 'Private'), ('personal-guests', 'Personal Guests'), ('family', 'Family'), ('family-guests', 'Family Guests'), ('public', 'Public')], max_length=255),
        ),
        migrations.DeleteModel(
            name='PrivateRoom',
        ),
    ]