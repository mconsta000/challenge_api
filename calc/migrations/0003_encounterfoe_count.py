# Generated by Django 2.2.4 on 2019-09-14 21:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calc', '0002_auto_20190914_1703'),
    ]

    operations = [
        migrations.AddField(
            model_name='encounterfoe',
            name='count',
            field=models.IntegerField(default=1),
        ),
    ]
