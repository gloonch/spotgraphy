# Generated by Django 2.2 on 2020-08-16 13:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SavedSpot',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'saved_spot',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Spot',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('latitude', models.TextField()),
                ('longitude', models.TextField()),
                ('description', models.TextField()),
                ('likes', models.IntegerField()),
                ('dislikes', models.IntegerField()),
                ('comments', models.IntegerField()),
            ],
            options={
                'db_table': 'spot',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateField(auto_created=True, auto_now=True, null=True)),
                ('name', models.TextField()),
                ('email', models.TextField()),
                ('token', models.TextField()),
            ],
            options={
                'db_table': 'user',
                'managed': False,
            },
        ),
    ]