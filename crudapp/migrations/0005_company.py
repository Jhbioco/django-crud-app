# Generated by Django 4.1.3 on 2022-12-03 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crudapp', '0004_alter_book_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
    ]