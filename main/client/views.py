from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from main import models



class CreateClientView(LoginRequiredMixin, View):
    def get(self, request):
        return render(request, 'client/create.html')
    
    def post(self, request):
        models.Client.objects.create(
            first_name=request.POST.get('first-name'),
            last_name=request.POST.get('last-name'),
            phone=request.POST.get('phone'),
            passport=request.POST.get('passport')
        )
        return redirect('main:home')
    

class ListClientView(View):
    def get(self, request):
        clients_list = models.Client.objects.all()
        return render(request, 'client/list.html', {'clients_list':clients_list})    


class DetailUpdateClientView(View):
    def get(self, request, id):
        client = models.objects.get(id=id)
        return render(request, 'client/detail.html', {'client':client})
    
    def post(self, request, id):
        client = models.Client.objects.get(id=id)
        client.first_name = request.POST.get('first-name')
        client.last_name = request.POST.get('last-name')
        client.phone = request.POST.get('phone')
        client.passport = request.POST.get('passport')
        client.save()
        return redirect('main:home')
    

class DeleteClientView(View):
    def get(self, request, id):
        models.Client.objects.get(id=id).delete()
        return redirect('main:home')