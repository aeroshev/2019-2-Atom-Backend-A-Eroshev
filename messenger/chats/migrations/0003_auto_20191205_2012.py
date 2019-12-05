# Generated by Django 2.2.5 on 2019-12-05 20:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('chats', '0002_member_last_read_message'),
        ('message', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='chat',
            name='creator',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='chat',
            name='last_message',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='Chat', to='message.Message'),
        ),
    ]
