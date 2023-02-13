# Generated by Django 4.1.1 on 2023-02-13 08:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Poin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_user', models.IntegerField()),
                ('email', models.EmailField(max_length=50, unique=True)),
                ('poin', models.IntegerField(default=0)),
            ],
        ),
    ]
