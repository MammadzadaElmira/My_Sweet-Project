# Generated by Django 5.1.1 on 2024-10-01 07:36

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('desert', '0027_alter_rating_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip_address', models.GenericIPAddressField()),
                ('recipe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='desert.recipe')),
            ],
        ),
    ]
