from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from appProva.utils import importar_sabates
from .forms import *
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

from appProva.utils import importar_sabates
from .forms import *





# Create your views here.

def home(request):

    return render(request, 'base.html')

def page2(request):
    dades_api = importar_sabates()
    print("ENTRAT PAG 2")
    print(dades_api)
    return render(request, 'page2.html', {'dades':dades_api})

def register(request):
    form = RegisterForm()
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            Usuari.objects.create(usuari=user)
            return render(request, 'register.html', {'form':form, 'message': 'Usuari creat correctament'})


    return render(request, 'register.html', {'form':form})

def login_user(request):
    form = LoginForm()
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.error(request, "Error a l'iniciar sessió")

    return render(request, 'login.html',{'form':form})


@login_required
def sabata_review(request):
    sabata = Sabata.objects.first()
    reviews = Review.objects.filter(producte=sabata)

    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            nova_review = form.save(commit=False)
            nova_review.user = request.user.username
            nova_review.producte = sabata
            nova_review.save()
            return redirect('sabata_detail')
    else:
        form = ReviewForm()

    return render(request, 'sabata_detail.html', {
        'sabata': sabata,
        'reviews': reviews,
        'form': form
    })


#def importar_dades(self, *args, **kwargs):
 #   importar_sabates()