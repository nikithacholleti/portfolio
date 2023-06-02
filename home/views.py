from django.shortcuts import render, HttpResponse
from home.models import Contact, Resume
import mimetypes
import os
from django.contrib import messages


# Create your views here.


def index(request):
    if request.method == 'POST':
        a = 1

    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')


def contact(request):
    print("hi")
    print(request)

    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        print(name, email, phone, message)
        con = Contact(name=name, email=email, phone=phone, message=message)
        con.save()
        messages.success(request, "message sent successfully")

    return render(request, 'contact.html')


def experiences(request):
    return render(request, 'experiences.html')


def certifications(request):
    return render(request, 'certifications.html')


def projects(request):
    return render(request, 'projects.html')


def skills(request):
    return render(request, 'skills.html')


def achievements(request):
    return render(request, 'achievements.html')


def links(request):
    return HttpResponse("this is links")
