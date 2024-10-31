from django.shortcuts import render
from selenium import webdriver

def index(request):
    return render(request, 'index.html')
