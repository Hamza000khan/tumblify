# Generated by Django 3.1.7 on 2021-03-03 18:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('api', '0018_auto_20210303_2331'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogs',
            name='Blogger',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.blogger'),
        ),
        migrations.AlterField(
            model_name='blogs',
            name='Bookmark',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bookmark', to='api.blog'),
        ),
        migrations.AlterField(
            model_name='blogs',
            name='added_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='blogs',
            name='content',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.blog'),
        ),
        migrations.AlterField(
            model_name='blogs',
            name='gist_embed',
            field=models.ForeignKey(max_length=200, on_delete=django.db.models.deletion.CASCADE, related_name='gist_e', to='api.blog'),
        ),
        migrations.AlterField(
            model_name='blogs',
            name='image_embed',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='image_e', to='api.blog'),
        ),
        migrations.AlterField(
            model_name='blogs',
            name='images',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.images'),
        ),
        migrations.AlterField(
            model_name='blogs',
            name='video_embed',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='video_e', to='api.blog'),
        ),
    ]
