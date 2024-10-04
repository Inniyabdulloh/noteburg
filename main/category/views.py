from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from main import models


class CreateCategoryView(LoginRequiredMixin, View):
    def get(self, request):
        return render(request, 'category/create.html')
    
    def post(self, request):
        models.Category.objects.create(
            name=request.POST.get('category')
        )

        return redirect('main:home')


class ListCategoryView(View):
    def get(self, request):
        category_list = models.Category.objects.all()
        return render(request, 'category/list.html', {'category_list':category_list})


class DetailUpdateCategoryView(View):
    def get(self, request, id):
        category = models.Category.objects.get(id=id)
        return render(request, 'category/detail.html')
    
    def post(self, request, id):
        category = models.Category.objects.get(id=id)
        category.name = request.POST.get('new-name')
        category.save()
        return render('main:home')
    

class DeleteCategoryView(View):
    def post(self, request, id):
        models.Category.objects.get(id=id).delete()
        return redirect('main:home')