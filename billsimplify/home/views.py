from django.shortcuts import render, HttpResponse

def index(request):
    context={
        "name_of_project":"Online Uniform Ordering System",
        "developers": "Kiran Chadde & Anushri Kudkyal",
        "project_status":"Working"
    }
    return render(request, "index.html",context)
    
    # return HttpResponse("This is home page")

def services(request):
    return render(request, "services.html")

def about(request):
    return render(request, "about.html")

def contact(request):
    return render(request, "contact.html")
# Create your views here.
