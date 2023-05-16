# Generated by Django 4.2 on 2023-05-15 13:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Logos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='tournaments_logos')),
            ],
        ),
        migrations.CreateModel(
            name='Participant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstName', models.CharField(max_length=100)),
                ('lastName', models.CharField(max_length=100)),
                ('thirdName', models.CharField(blank=True, max_length=100)),
                ('year', models.CharField(max_length=30)),
                ('discharge', models.CharField(max_length=40)),
                ('discharge_en', models.CharField(max_length=40, null=True)),
                ('discharge_ru', models.CharField(max_length=40, null=True)),
                ('gender', models.CharField(choices=[('Мужской', 'Мужской'), ('Женский', 'Женский')], max_length=10)),
                ('coach', models.CharField(blank=True, max_length=245)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Sponsors',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, upload_to='sponsors')),
            ],
        ),
        migrations.CreateModel(
            name='Tournament',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('title_en', models.CharField(max_length=100, null=True)),
                ('title_ru', models.CharField(max_length=100, null=True)),
                ('slug', models.SlugField(max_length=100, unique=True)),
                ('logo', models.ImageField(blank=True, upload_to='tournament_logo')),
                ('about', models.TextField(blank=True, max_length=1000)),
                ('about_en', models.TextField(blank=True, max_length=1000, null=True)),
                ('about_ru', models.TextField(blank=True, max_length=1000, null=True)),
                ('rang', models.CharField(blank=True, choices=[('Клубный', 'Клубный'), ('Городской', 'Городской'), ('Областной', 'Областной'), ('Региональный', 'Региональный'), ('Республиканский', 'Республиканский'), ('Чемпионат РК', 'Чемпионат РК'), ('Международный турнир', 'Международный турнир')], max_length=40)),
                ('rang_en', models.CharField(blank=True, choices=[('Клубный', 'Клубный'), ('Городской', 'Городской'), ('Областной', 'Областной'), ('Региональный', 'Региональный'), ('Республиканский', 'Республиканский'), ('Чемпионат РК', 'Чемпионат РК'), ('Международный турнир', 'Международный турнир')], max_length=40, null=True)),
                ('rang_ru', models.CharField(blank=True, choices=[('Клубный', 'Клубный'), ('Городской', 'Городской'), ('Областной', 'Областной'), ('Региональный', 'Региональный'), ('Республиканский', 'Республиканский'), ('Чемпионат РК', 'Чемпионат РК'), ('Международный турнир', 'Международный турнир')], max_length=40, null=True)),
                ('place', models.CharField(blank=True, max_length=100)),
                ('place_en', models.CharField(blank=True, max_length=100, null=True)),
                ('place_ru', models.CharField(blank=True, max_length=100, null=True)),
                ('startData', models.CharField(blank=True, max_length=100)),
                ('finishData', models.CharField(blank=True, max_length=100)),
                ('startTime', models.CharField(blank=True, max_length=10)),
                ('credit', models.CharField(blank=True, choices=[('личный', 'личный'), ('командный', 'командный')], max_length=100)),
                ('credit_en', models.CharField(blank=True, choices=[('личный', 'личный'), ('командный', 'командный')], max_length=100, null=True)),
                ('credit_ru', models.CharField(blank=True, choices=[('личный', 'личный'), ('командный', 'командный')], max_length=100, null=True)),
                ('tatamis_count', models.CharField(blank=True, default=0, max_length=2)),
                ('chiefJustice', models.CharField(blank=True, max_length=200)),
                ('chiefJustice_en', models.CharField(blank=True, max_length=200, null=True)),
                ('chiefJustice_ru', models.CharField(blank=True, max_length=200, null=True)),
                ('chiefSecretary', models.CharField(blank=True, max_length=200)),
                ('chiefSecretary_en', models.CharField(blank=True, max_length=200, null=True)),
                ('chiefSecretary_ru', models.CharField(blank=True, max_length=200, null=True)),
                ('status', models.CharField(choices=[('Регистрация открыта', 'Регистрация открыта'), ('Регистрация завершенa', 'Регистрация завершенa')], default='Регистрация_открыта', max_length=40)),
                ('public', models.BooleanField(default=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('logos', models.ManyToManyField(blank=True, default=[], related_name='logos', to='base.logos')),
                ('participants', models.ManyToManyField(blank=True, default=[], to='base.participant')),
                ('sponsors', models.ManyToManyField(blank=True, default=[], related_name='sponsors', to='base.sponsors')),
                ('user', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-updated', '-created'],
            },
        ),
        migrations.CreateModel(
            name='Weight',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
                ('participants', models.ManyToManyField(blank=True, default=[], to='base.participant')),
            ],
        ),
        migrations.CreateModel(
            name='WeightCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.CharField(blank=True, max_length=20)),
                ('gender', models.CharField(blank=True, choices=[('Мужской', 'Мужской'), ('Женский', 'Женский')], max_length=20)),
                ('gender_en', models.CharField(blank=True, choices=[('Мужской', 'Мужской'), ('Женский', 'Женский')], max_length=20, null=True)),
                ('gender_ru', models.CharField(blank=True, choices=[('Мужской', 'Мужской'), ('Женский', 'Женский')], max_length=20, null=True)),
                ('tournament', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='base.tournament')),
                ('weight', models.ManyToManyField(default=[], to='base.weight')),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullName', models.CharField(blank=True, max_length=100)),
                ('fullName_en', models.CharField(blank=True, max_length=100, null=True)),
                ('fullName_ru', models.CharField(blank=True, max_length=100, null=True)),
                ('phone', models.CharField(blank=True, max_length=12)),
                ('userType', models.CharField(choices=[('Админ', 'Админ'), ('Секретарь', 'Секретарь'), ('Свободный', 'Свободный')], default='Свободный', max_length=20)),
                ('userType_en', models.CharField(choices=[('Админ', 'Админ'), ('Секретарь', 'Секретарь'), ('Свободный', 'Свободный')], default='Свободный', max_length=20, null=True)),
                ('userType_ru', models.CharField(choices=[('Админ', 'Админ'), ('Секретарь', 'Секретарь'), ('Свободный', 'Свободный')], default='Свободный', max_length=20, null=True)),
                ('image', models.ImageField(blank=True, upload_to='profile_avatars')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
