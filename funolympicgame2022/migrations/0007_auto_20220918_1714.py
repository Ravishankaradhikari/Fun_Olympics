# Generated by Django 3.2 on 2022-09-18 11:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('funolympicgame2022', '0006_auto_20220918_1711'),
    ]

    operations = [
        migrations.AlterField(
            model_name='schedule',
            name='game1',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='schedule',
            name='game2',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='schedule',
            name='game3',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]
