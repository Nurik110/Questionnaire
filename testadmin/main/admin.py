from django.contrib import admin
from .models import People
from .models import PeopleProfile
from .models import Profile
# Register your models here.

admin.site.register(People)
admin.site.register(PeopleProfile)
admin.site.register(Profile)
