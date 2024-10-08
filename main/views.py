from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from . import models
# Create your views here.

def index(request):
    return render(request, 'index.html')
    


