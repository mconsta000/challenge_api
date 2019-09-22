# Generated by Django 2.2.4 on 2019-09-15 15:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('calc', '0003_encounterfoe_count'),
    ]

    operations = [
        migrations.CreateModel(
            name='FoeEncounters',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.IntegerField(default=1)),
                ('foe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='calc.Foe')),
            ],
        ),
        migrations.DeleteModel(
            name='EncounterFoe',
        ),
        migrations.AddField(
            model_name='encounter',
            name='foes',
            field=models.ManyToManyField(to='calc.FoeEncounters'),
        ),
    ]