# Generated by Django 3.2.8 on 2023-09-24 01:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0003_signvideo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='signvideo',
            name='word',
            field=models.CharField(max_length=50),
        ),
    ]
