# Generated by Django 5.0.6 on 2024-08-12 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('desert', '0002_comment_recipe'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='recipe',
            options={'verbose_name': 'Resept', 'verbose_name_plural': 'Resepts'},
        ),
        migrations.AddField(
            model_name='recipe',
            name='language',
            field=models.CharField(blank=True, choices=[('AZ', 'AZ'), ('EN', 'EN'), ('RU', 'RU')], max_length=4, null=True),
        ),
    ]
