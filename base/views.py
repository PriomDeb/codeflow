from django.shortcuts import render

# Create your views here.


rooms = [
    {'id':1, 'name': 'Learn Python'},
    {'id':2, 'name': 'Learn Django'},
    {'id':3, 'name': 'Learn Tkinter'},
]


def home(request):
    context = {'room':rooms}
    return render(request, 'base/home.html', context)

def room(request, pk):
    return render(request, 'base/room.html')