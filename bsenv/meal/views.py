from django.shortcuts import render
from django.utils import timezone
from .models import Token
from .forms import TokenForm
# Create your views here.
def index(request):
    return render(request,"index.html")
def menu(request):
    return render(request,"menu.html")
def token_list(request):
    tokens = Token.objects.all()
    return render(request, "token_list.html", {'tokens': tokens})
def registration(request):
    # if request.method == "POST":
    #     form = TokenForm(request.POST)
    #     if form.is_valid():
    #         token = form.save(commit=False)
    #         token.empName = request.user
    #         token.empId = request.user
    #         token.meal_date = timezone.now()
    #         token.save()
    #     return redirect('/')
    return render(request, 'registration.html')
