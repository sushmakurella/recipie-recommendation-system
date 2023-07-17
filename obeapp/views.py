from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from .forms import NewUserForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required

@login_required(login_url='/admin_login')
def admin_dashboard(request):
    return render(request, 'obeapp/admin_hods_dashboard.html')

def faculty_dashboard(request):
    return render(request, 'obeapp/faculty/faculty_dashboard.html')

def lessonplans(request):
    return render(request, 'obeapp/faculty/lessonplans.html')
def courses(request):
    return render(request, 'obeapp/faculty/courses.html')
def textref(request):
    return render(request, 'obeapp/faculty/textref.html')
def profmatrix(request):
    return render(request, 'obeapp/faculty/profmatrix.html')
def lectureplan(request):
    return render(request, 'obeapp/faculty/lectureplan.html')
def copsomatrix(request):
    return render(request, 'obeapp/faculty/copsomatrix.html')
def endsurveyquesnr(request):
    return render(request, 'obeapp/faculty/endsurveyquesnr.html')
def test(request):
    return render(request, 'obeapp/faculty/test.html')



def admin_login(request):
    if request.user.is_authenticated:
        return redirect(admin_dashboard)
    if request.method == "POST":
        uname = request.POST['uname']
        pswd = request.POST['pswd']
        user = authenticate(request, username=uname, password=pswd)
        if user and user.is_superuser:
            login(request, user)
            request.session['user_name'] = uname
            return redirect(admin_dashboard)
        else:
            return render(request, 'obeapp/admin_login.html', {'error': True})
    return render(request, 'obeapp/admin_login.html')

def admin_logout(request):
    logout(request)
    return redirect(login_request)

def faculty_registration(request):
    if request.method == 'POST':
        form = NewUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('admin_login')
    else:
        form = NewUserForm()
    return render(request, 'obeapp/faculty_registration.html', {'form': form})

def login_request(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'obeapp/index.html', {'error': 'Invalid credentials'})
    return render(request, 'obeapp/index.html')

def logout_request(request):
    logout(request)
    messages.info(request, "You have successfully logged out.")
    return redirect(login_request)




from .forms import PersonForm
from .models import Person
from django import forms

def editable_table(request):
    PersonFormSet = forms.formset_factory(PersonForm, extra=1)

    if request.method == 'POST':
        formset = PersonFormSet(request.POST, prefix='person')
        if formset.is_valid():
            for form in formset:
                name = form.cleaned_data['name']
                age = form.cleaned_data['age']
                email = form.cleaned_data['email']
                person, created = Person.objects.get_or_create(name=name, age=age, email=email)
            return redirect('editable_table')  # Redirect to the same page after saving
    else:
        formset = PersonFormSet(prefix='person', queryset=Person.objects.none())

    
    return render(request, 'obeapp/editable_table.html', {'formset': formset})


# from django.db import models
# # from django.apps import apps
# # from dynamic_models.models import ModelSchema, FieldSchema
# from django.shortcuts import render, redirect
# # from .forms import AdminForm
# # # from django.contrib.auth.models import dynamic_models_book
# from django.contrib.auth.decorators import login_required
# from .forms import NewUserForm
# from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
# from django.contrib.auth import login, authenticate, logout
# # import requests
# # from bs4 import BeautifulSoup
# from django.contrib import messages
# from django.contrib.auth.forms import AuthenticationForm
# # from datetime import datetime

# # print(datetime.now)
# # headers = {
# #     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
# # # Create your views here.


# # def home(request):
# #     return render(request, 'obeapp/home.html')


# # @login_required(login_url='/adminlog')
# # def index(request):
# #     return render(request, 'obeapp/index.html')
# # def admin_login(request):
# #     return render(request, 'obeapp/admin_login.html')
# @login_required(login_url='/admin_login')
# def admin_dashboard(request):
#     return render(request, 'obeapp/admin_hods_dashboard.html')
# def faculty_dashboard(request):
#     return render(request, 'obeapp/faculty/faculty_dashboard.html')
# def lessonplans(request):
#     return render(request, 'obeapp/faculty/lessonplans.html')



# def admin_login(request):
#     if request.user.is_authenticated:
#         return redirect(admin_dashboard)
#     if request.method == "POST":
#         uname = request.POST['uname']
#         pswd = request.POST['pswd']
#         user = authenticate(request, username=uname, password=pswd)
#         if user and user.is_superuser:
#             auth_login(request, user)
#             request.session['user_name'] = uname
#             return redirect(admin_dashboard)
#         else:
#             return render(request, 'obeapp/admin_login.html', {'error': True})
#     return render(request, 'obeapp/admin_login.html',)


# def admin_logout(request):
#     auth_logout(request)
#     return redirect(login_request)


# def faculty_registration(request):
#     if request.method == 'POST':
#         form = NewUserForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('admin_login')
#     else:
#         print("Please enter")
#     form = NewUserForm()
#         # placeholder = ["Username", "Email", "Designation",
#         #            "Date Of Joinning", "Biometric Id", "Password","Confirm"]
#     return render(request=request, template_name="obeapp/faculty_registration.html", context={"form":form})
#     # if request.method == "POST":
#     #     form = NewUserForm(request.POST)
#     #     if form.is_valid():
#     #         user = form.save()
#     #         messages.success(request, "Registration successful.")
#     #         print("Registration successful.")
#     #         return redirect(admin_login)
#     #     messages.error(
#     #         request, "Unsuccessful registration. Invalid information.")
#     #     print("Unsuccessful registration. Invalid information.")
#     # form = NewUserForm()
#     # placeholder = ["Username", "Email", "Designation",
#     #                "Date Of Joinning", "Biometric Id", "Password"]
#     # # placeholder = {"username":"Username", "email":"Email","Designation":"Designation","DateofJoinning":"Date Of Joinning","Biometricid":"Biometric Id","password":"Password"}
#     # return render(request=request, template_name="obeapp/faculty_registration.html", context={"sample": zip(form, placeholder)})
# # def faculty_registration(request):
# #     if request.method == "POST":
# #         form = NewUserForm(request.POST)
# #         if form.is_valid():
# #             user = form.save()
# #             messages.success(request, "Registration successful.")
# #             print("Registration successful.")
# #             return redirect(admin_login)
# #         messages.error(
# #             request, "Unsuccessful registration. Invalid information.")
# #         print("Unsuccessful registration. Invalid information.")
# #     form = NewUserForm()
# #     placeholder = ["Username", "Email", "Designation",
# #                    "Date Of Joinning", "Biometric Id", "Password"]
# #     # placeholder = {"username":"Username", "email":"Email","Designation":"Designation","DateofJoinning":"Date Of Joinning","Biometricid":"Biometric Id","password":"Password"}
# #     return render(request=request, template_name="obeapp/faculty_registration.html", context={"sample": zip(form, placeholder)})


# def login_request(request):
#     global us
#     if request.method == 'POST':
#         username = request.POST.get('username')
#         password = request.POST.get('password')
#         user = authenticate(request, username=username, password=password)
#         if user is not None:
#             login(request, user)
#             return redirect('home')
#         else:
#             return render(request, 'obeapp/index.html', {'error': 'Invalid credentials'})
#     return render(request=request, template_name="obeapp/index.html")
#     #     form = AuthenticationForm(request, data=request.POST)
#     #     if form.is_valid():
#     #         username = form.cleaned_data.get('username')
#     #         password = form.cleaned_data.get('password')
#     #         user = authenticate(username=username, password=password)
#     #         if user is not None:
#     #             login(request, user)
#     #             # us=username
#     #             request.session['us'] = username
#     #             messages.info(request, "You are now logged in as"+username+".")
#     #             print("You are now logged in as"+username+".")
#     #             return redirect(faculty_dashboard)

#     #         else:
#     #             print("valid")
#     #             messages.error(request, "Invalid username or password.")
#     #             print("Invalid username or password.")
#     #     else:
#     #         print("invalid")
#     #         messages.error(request, "Invalid username or password.")
#     #         print("Invalid username or password.")
#     # form = AuthenticationForm()
#     # return render(request=request, template_name="obeapp/index.html", context={"login_form": form})
# # def login_request(request):
# #     global us
# #     if request.method == "POST":
# #         form = AuthenticationForm(request, data=request.POST)
# #         if form.is_valid():
# #             username = form.cleaned_data.get('username')
# #             password = form.cleaned_data.get('password')
# #             user = authenticate(username=username, password=password)
# #             if user is not None:
# #                 login(request, user)
# #                 # us=username
# #                 request.session['us'] = username
# #                 messages.info(request, "You are now logged in as"+username+".")
# #                 print("You are now logged in as"+username+".")
# #                 return redirect(faculty_dashboard)

# #             else:
# #                 print("valid")
# #                 messages.error(request, "Invalid username or password.")
# #                 print("Invalid username or password.")
# #         else:
# #             print("invalid")
# #             messages.error(request, "Invalid username or password.")
# #             print("Invalid username or password.")
# #     form = AuthenticationForm()
# #     return render(request=request, template_name="obeapp/index.html", context={"login_form": form})


# def logout_request(request):
#     logout(request)
#     messages.info(request, "You have successfully logged out.")
#     return redirect(login_request)
