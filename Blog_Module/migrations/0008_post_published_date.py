# Generated by Django 4.2.2 on 2023-06-22 14:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Blog_Module', '0007_remove_post_published_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='published_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]