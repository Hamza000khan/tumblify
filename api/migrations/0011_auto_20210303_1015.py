# Generated by Django 3.1.7 on 2021-03-03 04:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0010_remove_blog_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='images',
            old_name='blog',
            new_name='Blog',
        ),
        migrations.CreateModel(
            name='Blogs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('blog', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.blog')),
                ('blogger', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.blogger')),
                ('images', models.ManyToManyField(to='api.Images')),
            ],
        ),
    ]
