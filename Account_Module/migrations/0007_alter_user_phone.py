# Generated by Django 4.2.2 on 2023-06-11 12:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Account_Module', '0006_alter_user_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='phone',
            field=models.IntegerField(unique=True),
        ),
    ]
