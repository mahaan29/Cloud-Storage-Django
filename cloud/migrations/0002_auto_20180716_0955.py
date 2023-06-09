# Generated by Django 2.0.7 on 2018-07-16 09:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cloud', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='audiodata',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('description', models.CharField(max_length=20)),
                ('browse', models.FileField(default='', upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='filedata',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('description', models.CharField(max_length=20)),
                ('browse', models.FileField(default='', upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='photodata',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('description', models.CharField(max_length=20)),
                ('browse', models.FileField(default='', upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='videodata',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('description', models.CharField(max_length=20)),
                ('browse', models.FileField(default='', upload_to='')),
            ],
        ),
        migrations.RenameField(
            model_name='customer',
            old_name='username',
            new_name='user_name',
        ),
    ]
