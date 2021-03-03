# Generated by Django 3.1.7 on 2021-03-03 10:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('api', '0013_blogs'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blogs',
            name='blogger',
        ),
        migrations.AddField(
            model_name='blogs',
            name='user',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]