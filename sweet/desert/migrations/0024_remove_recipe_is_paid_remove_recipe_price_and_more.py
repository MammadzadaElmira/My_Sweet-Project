# Generated by Django 5.1.1 on 2024-09-24 18:10

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('desert', '0023_paidrecipe_delete_login_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recipe',
            name='is_paid',
        ),
        migrations.RemoveField(
            model_name='recipe',
            name='price',
        ),
        migrations.CreateModel(
            name='SpecialRecipe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('recipe_name', models.CharField(blank=True, max_length=256, null=True)),
                ('instruction', models.TextField(blank=True, max_length=1000, null=True)),
                ('ingredients', models.TextField(blank=True, max_length=1000, null=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='desert.category')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='PaidRecipe',
        ),
    ]
