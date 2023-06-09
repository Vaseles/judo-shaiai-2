# Generated by Django 4.2.1 on 2023-06-02 14:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='participant',
            old_name='discharge_eng',
            new_name='discharge_en',
        ),
        migrations.RenameField(
            model_name='participant',
            old_name='discharge_kaz',
            new_name='discharge_kz',
        ),
        migrations.RenameField(
            model_name='participant',
            old_name='discharge_rus',
            new_name='discharge_ru',
        ),
        migrations.RenameField(
            model_name='profile',
            old_name='fullName_eng',
            new_name='fullName_en',
        ),
        migrations.RenameField(
            model_name='profile',
            old_name='fullName_kaz',
            new_name='fullName_kz',
        ),
        migrations.RenameField(
            model_name='profile',
            old_name='fullName_rus',
            new_name='fullName_ru',
        ),
        migrations.RenameField(
            model_name='profile',
            old_name='userType_eng',
            new_name='userType_en',
        ),
        migrations.RenameField(
            model_name='profile',
            old_name='userType_kaz',
            new_name='userType_kz',
        ),
        migrations.RenameField(
            model_name='profile',
            old_name='userType_rus',
            new_name='userType_ru',
        ),
        migrations.RenameField(
            model_name='tournament',
            old_name='about_eng',
            new_name='about_en',
        ),
        migrations.RenameField(
            model_name='tournament',
            old_name='about_kaz',
            new_name='about_kz',
        ),
        migrations.RenameField(
            model_name='tournament',
            old_name='about_rus',
            new_name='about_ru',
        ),
        migrations.RenameField(
            model_name='tournament',
            old_name='chiefJustice_eng',
            new_name='chiefJustice_en',
        ),
        migrations.RenameField(
            model_name='tournament',
            old_name='chiefJustice_kaz',
            new_name='chiefJustice_kz',
        ),
        migrations.RenameField(
            model_name='tournament',
            old_name='chiefJustice_rus',
            new_name='chiefJustice_ru',
        ),
        migrations.RenameField(
            model_name='tournament',
            old_name='chiefSecretary_eng',
            new_name='chiefSecretary_en',
        ),
        migrations.RenameField(
            model_name='tournament',
            old_name='chiefSecretary_kaz',
            new_name='chiefSecretary_kz',
        ),
        migrations.RenameField(
            model_name='tournament',
            old_name='chiefSecretary_rus',
            new_name='chiefSecretary_ru',
        ),
        migrations.RenameField(
            model_name='tournament',
            old_name='credit_eng',
            new_name='credit_en',
        ),
        migrations.RenameField(
            model_name='tournament',
            old_name='credit_kaz',
            new_name='credit_kz',
        ),
        migrations.RenameField(
            model_name='tournament',
            old_name='credit_rus',
            new_name='credit_ru',
        ),
        migrations.RenameField(
            model_name='tournament',
            old_name='place_eng',
            new_name='place_en',
        ),
        migrations.RenameField(
            model_name='tournament',
            old_name='place_kaz',
            new_name='place_kz',
        ),
        migrations.RenameField(
            model_name='tournament',
            old_name='place_rus',
            new_name='place_ru',
        ),
        migrations.RenameField(
            model_name='tournament',
            old_name='rang_eng',
            new_name='rang_en',
        ),
        migrations.RenameField(
            model_name='tournament',
            old_name='rang_kaz',
            new_name='rang_kz',
        ),
        migrations.RenameField(
            model_name='tournament',
            old_name='rang_rus',
            new_name='rang_ru',
        ),
        migrations.RenameField(
            model_name='tournament',
            old_name='title_eng',
            new_name='title_en',
        ),
        migrations.RenameField(
            model_name='tournament',
            old_name='title_kaz',
            new_name='title_kz',
        ),
        migrations.RenameField(
            model_name='tournament',
            old_name='title_rus',
            new_name='title_ru',
        ),
        migrations.RenameField(
            model_name='weightcategory',
            old_name='gender_eng',
            new_name='gender_en',
        ),
        migrations.RenameField(
            model_name='weightcategory',
            old_name='gender_kaz',
            new_name='gender_kz',
        ),
        migrations.RenameField(
            model_name='weightcategory',
            old_name='gender_rus',
            new_name='gender_ru',
        ),
    ]
