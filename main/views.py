from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from . import models
# Create your views here.

def index(request):
    return render(request, 'index.html')
    

class CreateRoom(LoginRequiredMixin, View):
    def get(self, request):
        return render(request, 'create-room.html')    
    
    def post(self, request):
        number = request.POST.get('number')
        room = models.Room.objects.get(number=request.POST.get('number'))
        if room:
            models.Room.objects.create(
                category=models.Category.objects.get(id=request.POST.get('category')),
                number=number,
                price=request.POST.get('price')
            )

        return redirect('main:home')


class BookingRoom(LoginRequiredMixin, View):
    def get(self, request):
        return render(request, 'booking-room.html')
    
    def post(self, request):
        room = models.Room.objects.get(id=request.POST.get('room'))
        client = models.Client.objects.get(id=request.POST.get('client'))
        models.BookedRoom.objects.create(
            room=room,
            client=client,
            admin=request.user,
            start_date=request.POST.get('start-date'),
            end_date=request.POST.get('end-date')
        )

        return redirect('main:home')
