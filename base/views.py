from django.shortcuts import render

# Create your views here.


rooms = [
    {'id':1, 'name': 'Learn Python'},
    {'id':2, 'name': 'Learn Django'},
    {'id':3, 'name': 'Learn Tkinter'},
]


def home(request):
    return render(request, 'home.html', {'room':rooms})

def room(request):
    return render(request, 'room.html')