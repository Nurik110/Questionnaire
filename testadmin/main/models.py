from django.db import models
from django import forms
import uuid
from django.core.validators import EmailValidator
from django.contrib.auth.models import User
from django.dispatch import receiver #add this
from django.db.models.signals import post_save #add this

emailvalidator = EmailValidator(message="invalid email")

class People(models.Model):
    id = models.CharField(primary_key=True,max_length=500, default=uuid.uuid4(), editable=False)
    username = models.CharField(verbose_name='Имя', max_length=500, default="")
    last_name = models.CharField(verbose_name='Фамилия', max_length=500, default="")
    email = models.EmailField(verbose_name='Email', validators=[emailvalidator])
    password = models.CharField(verbose_name='пароль1', max_length=20, default="")
    
    def __str__(self):
        return self.email

class PeopleProfile(models.Model): 
    # yesbox = "yes"
    # nobox = "no"
    # YES_NO_CHOICES = (
    #     (yesbox , "Yes"),
    #     (nobox, "No")
    # ), choices=YES_NO_CHOICES
    nickname = models.CharField(verbose_name='Имя', max_length=500, default="")
    butt = models.IntegerField(verbose_name='Кнопка')

    def __str__(self):
        return self.nickname

class Profile(models.Model):   #add this class and the following fields
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	peopleform = models.ManyToManyField(PeopleProfile)




@receiver(post_save, sender=User) #add this
def create_user_profile(sender, instance, created, **kwargs):
	if created:
		Profile.objects.create(user=instance)

@receiver(post_save, sender=User) #add this
def save_user_profile(sender, instance, **kwargs):
		instance.profile.save()
