# Generated by Django 3.2 on 2023-02-13 11:04

from django.db import migrations, models
import djongo.models.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Poin',
            fields=[
                ('_id', djongo.models.fields.ObjectIdField(auto_created=True, primary_key=True, serialize=False)),
                ('id_user', models.CharField(max_length=128)),
                ('nama', models.CharField(max_length=64)),
                ('email', models.EmailField(max_length=50, unique=True)),
                ('poin', models.IntegerField(default=0)),
            ],
        ),
    ]