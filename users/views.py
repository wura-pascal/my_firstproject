from django.shortcuts import render
from django.http import HttpResponse
from . models import User, Wura
from .forms import Users_Form, NameForm


# Create your views here.

def index(request):
    return HttpResponse("Hello, world!!")

def create_user(request):

    if request.method == "POST": # when the form is submitted
        form = forms.Users_Form(request.POST)

        if form.is_valid():
            first_name = form.cleaned_data
        


        
    form = Users_Form()
    return render(request, "users/signup.html", {"form": form})
        # first_name ="Adio"
        # last_name = "Mustapha"
        # email = "wurapascal@gmail.com"

        # user = User ()
        # user.first_name = first_name
        # user.last_name = last_name
        # user.email = email
        # user.save()

        # return HttpResponse("user created")


# def create_wura(request):
    if request.method == 'POST':
        form = forms.NameForm(request.POST)
    
          
    form = NameForm()
    return render(request, "users/created.html", {"form": form})      


    if request.method == 'POST':
        form = forms.wura_ruth(request.POST)
    
          
    form = Wura_Form()
    return render(request, "users/name.html", {"form": form})   





def get_name(request):
    if request.method == "POST":
        form = NameForm(request.POST)
        if form.is_valid():
            full_name = form.cleaned_data['full_name']
            age = form.cleaned_data['age']
            class_grade = form.cleaned_data['class_grade']
            name_school = form.cleaned_data['name_school']
            wura = Wura()
            
            wura.name_school = name_school
            wura.save()
            return HttpResponse("/thanks/")

    else:
        form = NameForm()

    return render(request, "users/name.html", {"form": form})

def signup(request):
    return render(request, 'users/signup.html')