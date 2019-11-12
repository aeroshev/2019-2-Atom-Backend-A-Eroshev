# Generated by Django 2.2.5 on 2019-11-12 21:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chats', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chat',
            name='is_group_chat',
            field=models.BooleanField(verbose_name='Group chat'),
        ),
        migrations.AlterField(
            model_name='chat',
            name='last_message',
            field=models.TextField(null=True, verbose_name='Last message'),
        ),
    ]
