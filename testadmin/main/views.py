from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseForbidden
from .models import PeopleProfile  
from django.contrib.auth.models import User
from users.forms import RegisterForm  
# from django.shortcuts import redirect
# from django.utils import timezone
from django.contrib import auth
from .forms import UserForm, ProfileForm, PersonForm #import UserForm and ProfileForm  +++NewUserForm, 
from django.contrib.auth import authenticate, login
import json
import uuid

# Create your views here.
def index(request):
    if request.method == "POST":  
        # print('Hello')
        received_json_data=json.loads(request.body)
        user = User.objects.create_user(received_json_data['username'], received_json_data['email'], received_json_data['password'])
        user.save()
        # people_instance = People.objects.create(
        #     id=uuid.uuid4(),
        #     email=received_json_data['email'],
        #     username=received_json_data['username'],
        #     last_name=received_json_data['last_name'],
        #     password=received_json_data['password'],
        #     )
        print(received_json_data)
        return  HttpResponse("{}")
    else:
        return render(request, "index.html")
        
def login(request):
    if request.method == "POST":  
        # print('Hello')
        received_json_data=json.loads(request.body)
        email = received_json_data['emaill']
        password = received_json_data['passwordd']
        User = auth.authenticate(username=email, password=password)
        if User is not None and User.is_active:
        # Правильный пароль и пользователь "активен"
            auth.login(request, User)
        # Перенаправление на "правильную" страницу
            return  HttpResponse("{}")
        else:
        # Отображение страницы с ошибкой
            return HttpResponseForbidden()
    else:
        return render(request, "login.html")

def user(request):

	user_form = UserForm(instance=request.user)
	profile_form = ProfileForm(instance=request.user.profile)
	return render(request=request, template_name="main/user.html", context={"user":request.user, "user_form":user_form, "profile_form":profile_form })        

def result(request):
    return render(request, "result.html")

def questionnaire(request):
    hero = PeopleProfile.objects.all()
    if request.method == "POST":  
        # print('Hello')
        received_json_data=json.loads(request.body)
        # user = PeopleProfile.objects.create_user(received_json_data['nickname'], received_json_data['butt'])
        # user.save()
        people_instance = PeopleProfile.objects.create(
            # id=uuid.uuid4(),
            nickname=received_json_data['nickname'],
            butt=received_json_data['butt'],
        
            )
        print(received_json_data)
        return  HttpResponse("{}")
    else:
        return render(request, "questionnaire.html", context={'hero': hero, })  
      

# def my_view(request):
#     form = PersonForm(request.POST or None)
#     if request.method == "POST":
#         display_type = request.POST.get("display_type", None)
#         if display_type in ["yesbox", "nobox"]:
#             display_type = request.POST["display_type"]
#         else
#             request.POST["something_truthy"]:
#     else
#         return render(request, 'your_template.html', {'form': form})
