# Generated by Django 4.0.6 on 2022-09-27 16:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('funolympicgame2022', '0010_rename_newsp2_new_news_remove_new_newsp1'),
    ]

    operations = [
        migrations.RenameField(
            model_name='new',
            old_name='img1',
            new_name='image',
        ),
    ]
