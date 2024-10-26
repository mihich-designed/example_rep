# Generated by Django 5.0.7 on 2024-10-09 07:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book_app', '0018_alter_bookpicture_book'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='full_name',
            field=models.CharField(max_length=150, verbose_name='Полное имя'),
        ),
        migrations.AlterField(
            model_name='author',
            name='slug',
            field=models.SlugField(blank=True, default=''),
        ),
    ]