# Generated by Django 4.2.2 on 2023-06-22 14:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Blog_Module', '0005_remove_post_published_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='published_date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
