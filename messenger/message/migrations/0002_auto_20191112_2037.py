# Generated by Django 2.2.5 on 2019-11-12 20:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('message', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='message',
            old_name='chat',
            new_name='dialog',
        ),
        migrations.RenameField(
            model_name='message',
            old_name='user',
            new_name='userman',
        ),
    ]
