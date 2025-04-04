from django.shortcuts import render, get_object_or_404

from .models import Meeting

def detail(request, id):
    meeting = get_object_or_404(Meeting, pk=id)
    return render(request, "meetings/details.html", {"meeting": meeting})

def new(request):
    return render(request, "meetings/new.html")