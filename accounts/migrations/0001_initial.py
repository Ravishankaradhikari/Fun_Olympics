# Generated by Django 4.0.6 on 2022-09-21 17:38

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Gametype',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('auth_token', models.CharField(max_length=100)),
                ('is_verified', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Content',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(blank=True, default='', max_length=200, null=True)),
                ('desc', models.CharField(blank=True, default='', max_length=10000, null=True)),
                ('image', models.ImageField(null=True, upload_to='images_uploaded')),
                ('video', models.FileField(null=True, upload_to='videos_uploaded', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['MOV', 'avi', 'mp4', 'webm', 'mkv'])])),
                ('date_uploaded', models.DateTimeField(default=django.utils.timezone.now)),
                ('dislikes', models.ManyToManyField(blank=True, related_name='dislikes', to=settings.AUTH_USER_MODEL)),
                ('gametype', models.ForeignKey(default=1, null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.gametype')),
                ('likes', models.ManyToManyField(blank=True, related_name='likes', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('comment', models.TextField()),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.content')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]