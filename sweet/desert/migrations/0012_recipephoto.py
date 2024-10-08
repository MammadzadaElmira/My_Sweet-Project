# Generated by Django 5.0.6 on 2024-08-23 10:13

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('desert', '0011_recipe_created_at'),
    ]

    operations = [
        migrations.CreateModel(
            name='RecipePhoto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pht', models.ImageField(upload_to='recipes_photos/%Y/%m/%d')),
                ('photo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='photos', to='desert.recipe')),
            ],
        ),
    ]
