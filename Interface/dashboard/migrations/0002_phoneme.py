# Generated by Django 3.2.8 on 2023-09-23 13:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Phoneme',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', models.CharField(blank=True, max_length=5)),
                ('description', models.CharField(max_length=50)),
                ('example', models.CharField(max_length=50)),
                ('audio', models.FileField(blank=True, upload_to='phonemes/')),
            ],
        ),
    ]
