from datetime import datetime
from django.shortcuts import render
from django.http import HttpResponse

from meetings.models import Meeting
from room.models import Room

def welcome(request):
    return render(request, "website/welcome.html", {"meetings": Meeting.objects.all(), "rooms": Room.objects.all()})

def date(request):
    return HttpResponse("This page was served at" + str(datetime.now()))

def about(request):
    return HttpResponse("I am Dhruv and I am currently learning Django!")