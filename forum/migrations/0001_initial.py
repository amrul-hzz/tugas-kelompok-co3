# Generated by Django 4.1 on 2022-11-02 15:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creator_name', models.CharField(default='Unknown', max_length=255)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('content', models.TextField(max_length=255)),
                ('image', models.URLField()),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creator_name', models.CharField(default='Unknown', max_length=255)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('content', models.TextField(max_length=255)),
                ('original_post_id', models.PositiveIntegerField(default=0)),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
