from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from .models import Time
from django.urls import reverse_lazy

class SetAlarm(CreateView):
    model = Time
    fields = '__all__'
    success_url = reverse_lazy('confirm')
    template_name = 'base/homepage.html'

class ConfirmAlarm(ListView):
    model = Time
    template_name = 'base/confirmation.html'

