from django.db import models
from django.core.files.storage import default_storage
from modeltranslation.translator import TranslationOptions, register

from django.contrib.auth.models import User

# Auto Add
class Profile(models.Model):
   TASKS = (
      ('Админ', 'Админ'),
      ('Секретарь', 'Секретарь'),
      ('Свободный', 'Свободный')
   )
   user = models.OneToOneField(User, on_delete=models.CASCADE)
   
   fullName = models.CharField(max_length=100, blank=True)
   phone = models.CharField(max_length=12, blank=True)
   organization = models.CharField(max_length=300, blank=True)
   
   city = models.CharField(max_length=200, blank=True)
   region =  models.CharField(max_length=200, blank=True)
   
   userType = models.CharField(max_length=20, choices=TASKS, default='Свободный')
   image = models.ImageField(upload_to='profile_avatars', blank=True)
      
   created = models.DateTimeField(auto_now_add=True)
   updated = models.DateTimeField(auto_now=True)
   
   def __str__(self):
      return self.user.username
   
# Logotips Gallery
class Logos(models.Model):
   image = models.ImageField(upload_to='tournaments_logos')
   
   def __str__(self):
      return self.image.name
   
# Participants
class Participant(models.Model):
   GENDER = (
      ('Мужской', 'Мужской'),
      ('Женский', 'Женский')
   )
   user = models.ForeignKey(User, on_delete=models.CASCADE)
   firstName = models.CharField(max_length=100)
   lastName = models.CharField(max_length=100)
   thirdName = models.CharField(max_length=100, blank=True)
   
   year = models.CharField(max_length=30)
   discharge = models.CharField(max_length=40)
   gender = models.CharField(max_length=10, choices=GENDER)
   coach = models.CharField(max_length=245, blank=True)
   
   # country = models.CharField(max_length=100, blank=True)
   # city = models.CharField(max_length=100, blank=True)
   
   # weight = models.IntegerField(blank=True, default=0)
   
   created = models.DateTimeField(auto_now_add=True)
   updated = models.DateTimeField(auto_now=True)
   
   def __str__(self):
      return '{} {} {}'.format(self.firstName, self.lastName, self.thirdName)

# Sponsors Emblems or Names
class Sponsors(models.Model):
   image = models.ImageField(upload_to='sponsors', blank=True)
   
   def __str__(self):
      return self.image.name

# Tournament Translation
class TournamentTranslationOptions(TranslationOptions):
    fields = ('title', 'about', 'rang', 'credit', 'status')

# Tournament
class Tournament(models.Model):
   
   RANGS = (
      ('Клубный', 'Клубный'),
      ('Городской', 'Городской'),
      ('Областной', 'Областной'),
      ('Региональный', 'Региональный'),
      ('Республиканский', 'Республиканский'),
      ('Чемпионат РК', 'Чемпионат РК'),
      ('Международный турнир', 'Международный турнир'),
   )
   
   CREDIT_TYPE = (
      ('личный', 'личный'),
      ('командный', 'командный')
   )
   
   STATUS = (
      ('Регистрация открыта', 'Регистрация открыта'),
      ('Регистрация завершенa', 'Регистрация завершенa'),
   )
   
   user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
   title = models.CharField(max_length=100)
   slug = models.SlugField(max_length=100, unique=True)
   logo = models.ImageField(upload_to='tournament_logo', blank=True)
   logos = models.ManyToManyField(Logos, default=[], blank=True, related_name='logos')
   about = models.TextField(max_length=1000, blank=True)
   
   rang = models.CharField(max_length=40,choices=RANGS, blank=True)
   
   place = models.CharField(max_length=100, blank=True)
   
   startData = models.CharField(max_length=100, blank=True)
   finishData = models.CharField(max_length=100, blank=True)
   startTime = models.CharField(max_length=10, blank=True)

   credit = models.CharField(max_length=100, blank=True, choices=CREDIT_TYPE)
   
   tatamis_count = models.CharField(default=0, blank=True, max_length=2)
   
   # weight_categories = models.ManyToManyField(WeightCategory, blank=True, default=[])
   participants = models.ManyToManyField(Participant, default=[], blank=True)
   
   sponsors = models.ManyToManyField(Sponsors, blank=True, default=[], related_name='sponsors')
   
   chiefJustice = models.CharField(max_length=200, blank=True)
   chiefSecretary = models.CharField(max_length=200, blank=True)
   status = models.CharField(max_length=40, choices=STATUS, default='Регистрация_открыта')
   
   public = models.BooleanField(default=True)   
   
   created = models.DateTimeField(auto_now_add=True)
   updated = models.DateTimeField(auto_now=True)
      
   class Meta: 
      ordering = ['-updated', '-created']
      
   def delete(self):
      # Full Delete 
      logotips = self.logos.all()
      sponor_emblems = self.sponsors.all()
      
      for logotip in logotips:
         default_storage.delete(logotip.image.path)
         logotip.delete()
      
      for sponor_emblem in sponor_emblems:
         default_storage.delete(sponor_emblem.image.path)
         sponor_emblem.delete()
      
      super(Tournament, self).delete()    
   
   def __str__(self):
      return self.title
   
class Weight(models.Model):
   name = models.CharField(max_length=10)
   
   participants = models.ManyToManyField(Participant, default=[], blank=True)
   
   def __str__(self):
      return self.name 

# Tournament Translation
class WeightCategoryTranslationOptions(TranslationOptions):
    fields = ('gender',)

# Weight Category
class WeightCategory(models.Model):
   GENDER = (
      ('Мужской', 'Мужской'),
      ('Женский', 'Женский')
   )
   
   tournament = models.ForeignKey(Tournament, on_delete=models.CASCADE, blank=True)
   weight = models.ManyToManyField(Weight, default=[])
   
   year = models.CharField(max_length=20, blank=True)
   gender = models.CharField(max_length=20, blank=True, choices=GENDER)
      
   def delete(self):
      weights = self.weight.all()
      
      for w in weights:
         w.delete()
      
      super(WeightCategory, self).delete()    
      
   def __str__(self):
      return self.year 