# Generated by Django 5.0.6 on 2024-08-22 12:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('desert', '0010_remove_comment_created_at_recipe_category_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
