from django.shortcuts import render
from django.utils import timezone
from .models import Token
from .models import User
from .forms import TokenForm
from .forms import UserForm
# Create your views here.
def index(request):
    return render(request,"index.html")

def menu(request):
    return render(request,"menu.html")

def token_list(request):
    tokens = Token.objects.all()
    return render(request, "token_list.html", {'tokens': tokens})

def registration(request):
	form = TokenForm(request.POST)
	if request.method == 'POST':
		if form.is_valid():
			form.save()
			return index(request)
		else:
			form = TokenForm()
	return render(request,'registration.html',{'form':form})

def user(request):
	form = UserForm
	if request.method == 'POST':
		form = UserForm(request.POST)
		if form.is_valid():
			form.save(commit=True)
			return index(request)
		else:
			print("error! check model,view & form file.")
	return render(request,'user.html',{'form':form})

def profile_list(request):
    profiles = User.objects.all()
    return render(request, "profile.html", {'profiles': profiles})