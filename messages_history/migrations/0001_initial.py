# Generated by Django 5.1 on 2024-08-30 10:11

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('chat', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MessagesHistory',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('seller_message', models.TextField()),
                ('bot_message', models.TextField()),
                ('chat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='messages', to='chat.chat')),
            ],
        ),
    ]
