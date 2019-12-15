from django.shortcuts import render

# Create your views here.
def call_home(response):
    print("called")
    return render(response,"home.html",{})
