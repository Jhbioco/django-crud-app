# Generated by Django 4.1.3 on 2022-11-23 19:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crudapp', '0002_alter_book_options_book_created_at'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='book',
            options={'ordering': ['created_at']},
        ),
    ]