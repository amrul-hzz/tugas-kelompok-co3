# Generated by Django 4.1 on 2022-10-28 11:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        
        ('forum', '0002_comment_rename_post_post_content_remove_post_poster'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='creator',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='landing_page.useraccount'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.URLField(),
        ),
        migrations.AddField(
            model_name='comment',
            name='creator',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='landing_page.useraccount'),
        ),
        migrations.AddField(
            model_name='comment',
            name='original_post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='forum.post'),
        ),
    ]
