# Generated by Django 4.1.7 on 2023-04-11 03:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_alter_logos_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='weightcategory',
            name='slug',
            field=models.CharField(default='', max_length=50),
        ),
    ]