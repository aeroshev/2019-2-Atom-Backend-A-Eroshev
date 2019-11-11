# Generated by Django 2.2.5 on 2019-11-10 13:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=40)),
                ('nick', models.CharField(max_length=100)),
                ('avatar', models.CharField(max_length=100)),
                ('date_of_birthday', models.DateTimeField()),
            ],
        ),
    ]
