from django.shortcuts import render
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from .models import UserCredentials

def index(request):
    # options = Options()
    # target_url = "https://global.yunatt.com/staff/index"
    # driver = webdriver.Chrome(options=options)
    # start_url = "https://global.yunatt.com/"
    # driver.get(start_url)
    user_credentials = UserCredentials.objects.get(username='youssefmehyali67@gmail.com')
    print(user_credentials.password)
    return render(request, 'index.html')


