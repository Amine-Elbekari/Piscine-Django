from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import ChatRoom
# Create your views here.
@login_required
def room_view(request):
    rooms = ChatRoom.objects.all()
    return render(request, "chat/room.html", {"rooms": rooms})

@login_required
def chat_view(request, room_name):
    room = ChatRoom.objects.get(name=room_name)
    return render(request, "chat/chat.html", {"room": room})
