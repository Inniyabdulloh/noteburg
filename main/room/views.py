from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from main import models


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


class LIstRoomView(View):
    def get(self, request):
        rooms_list = models.Room.objects.all()
        return render(request, 'room/list.html', {'room_list':rooms_list})

class DetailUpdateView(View):
    def get(self, request, id):
        room = models.Room.objects.get(id=id)
        return render(request, 'room/update.html', {'room':room})
    
    def post(self, request, id):
        room = models.Room.objects.get(id=id)       
        room.category = models.Category.objects.get(id=request.POST.get('category'))
        number = request.POST.get('number')
        if room.number != number:
            has_number = models.Room.objects.get(number=number)
            if has_number:
                return redirect('main:home')
            room.number = number
        room.price = request.POST.get('price')
        room.save()  
        return redirect('main:home')  


class DeleteRoomView(View):
    def get(self, request, id):
        models.Room.objects.get(id=id).delete()
        return redirect('main:home')


            



class BookingRoom(LoginRequiredMixin, View):
    def get(self, request, id):
        room = models.Room.objects.get(id=id)
        return render(request, 'booking-room.html', {'room':room})
    
    def post(self, request, id):
        room = models.Room.objects.get(id=id)
        client = models.Client.objects.get(id=request.POST.get('client'))
        models.BookedRoom.objects.create(
            room=room,
            client=client,
            admin=request.user,
            start_date=request.POST.get('start-date'),
            end_date=request.POST.get('end-date')
        )

        return redirect('main:home')