from django.shortcuts import render
from .models import Room

# Create your views here.


# rooms = [
#     {'id':1, 'name': 'Learn Python'},
#     {'id':2, 'name': 'Learn Django'},
#     {'id':3, 'name': 'Learn Tkinter'},
# ]


def home(request):
    rooms = Room.objects.all()
    context = {'room':rooms}
    return render(request, 'base/home.html', context)

def room(request, pk):
    room = Room.objects.get(id=pk)
    
    context = {'rooms': room}
    return render(request, 'base/room.html', context)
