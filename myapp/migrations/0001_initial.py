# Generated by Django 2.1.15 on 2022-10-07 17:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('password', models.CharField(max_length=30)),
                ('username', models.CharField(max_length=30)),
                ('age', models.CharField(max_length=3)),
                ('sex', models.CharField(max_length=6)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
    ]