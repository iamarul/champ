from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
# Create your views here.
from models import Page


def home(request):
    page = Page.objects.get(name='home')
    section = page.section
    return render(request, section, {})