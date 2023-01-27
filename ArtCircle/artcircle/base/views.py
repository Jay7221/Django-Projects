from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.urls import reverse_lazy
from django.contrib.auth.models import User
# Create your views here.

from .models import Member, Event

class SignUp(CreateView):
    model = User
    fields = ['username', 'first_name', 'last_name', 'email']
    context_object_name = 'user'
    success_url = reverse_lazy('events')
    template_name = 'base/sign_up.html'

def loginPage(request):
    context = {}
    return render(request, 'login.html', context)


def signUp(request):
    context = {}
    return render(request, 'sign_up.html', context)


def homePage(request):
    return render(request, 'home.html')

class EventList(ListView):
    model = Event
    context_object_name = 'events'
    template_name = 'base/events.html'

class EventDetails(DetailView):
    model = Event
    context_object_name = 'event'

class EventCreate(CreateView):
    model = Event
    context_object_name = 'event'
    fields = '__all__'
    success_url = reverse_lazy('events')

class EventUpdate(UpdateView):
    model = Event
    context_object_name = 'event'
    fields = '__all__'
    success_url = reverse_lazy('events')

class EventDelete(DeleteView):
    model = Event
    context_object_name = 'event'
    success_url = reverse_lazy('events')

def viewMembers(request):
    members = Member.objects.all().values()
    context = {
        'members' : members
    }
    return render(request, 'members.html', context)

def memberProfile(request, pk):
    print("View Details Called", pk)
    member = Member.objects.get(id = pk)
    context = {
        'id' : pk,
        'member' : member
    }
    return render(request, 'profile.html', context)


def profileSettings(request, pk):
    context = {
        'id' : pk
    }
    return render(request, 'profile.html', context)