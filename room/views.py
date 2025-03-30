from django.shortcuts import render, get_object_or_404

from .models import Room

def room_detail(request, id):
    room = get_object_or_404(Room, pk=id)
    return render(request, "room/details.html", {"room": room})

def room_list(request):
    return render(request, "room/room_list.html", {"rooms": Room.objects.all()})
