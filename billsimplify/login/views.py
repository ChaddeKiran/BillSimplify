from django.shortcuts import render, HttpResponse

# Create your views here.
def login(request):
    return render(request, "login.html")
    # return HttpResponse("This is home page") 

def signup(request):
    return render(request, "signup.html")