# Generated by Django 4.2.2 on 2023-06-11 12:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Account_Module', '0002_alter_user_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='phone',
            field=models.EmailField(max_length=255, unique=True),
        ),
    ]