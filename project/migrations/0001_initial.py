# Generated by Django 5.1 on 2024-08-30 10:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(default=None, max_length=100)),
                ('projecttype', models.CharField(max_length=255)),
                ('description', models.TextField()),
            ],
        ),
    ]
