# Generated by Django 5.0.6 on 2024-08-26 13:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('desert', '0012_recipephoto'),
    ]

    operations = [
        migrations.RenameField(
            model_name='recipe',
            old_name='description',
            new_name='ingredient',
        ),
        migrations.AddField(
            model_name='recipe',
            name='instruction',
            field=models.TextField(blank=True, max_length=1000, null=True),
        ),
    ]
