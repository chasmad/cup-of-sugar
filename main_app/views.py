from django.shortcuts import render, redirect
from . models import Cup
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.detail import DetailView

# Create your views here.


class CupRead(DetailView):
    model = Cup
    fields = ['user_name', 'cup_type', 'item', 'category', 'description', 'fulfilled']

def home(request):
    return render(request, 'home.html')


def index(request):
    return render(request, 'cups/index.html')


def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
        else:
            error_message = 'Invalid sign up - try again'
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'registration/signup.html', context)
