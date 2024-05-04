from django.shortcuts import render

from django.http import HttpResponse

# def home(request):
#     return HttpResponse("<h1>Hey I am a django Server.</h1>")

def home(request):
    people = [
        {"name": "Abhilash", "age": 27},
        {"name": "Suraj", "age": 28},
        {"name": "Omkar", "age": 26},
        {"name": "Amol", "age": 17}
    ]
    text = "Abhilash"
    return render(request , "index.html", context={"page":"Home","people_lst": people, "txt": text})

def success_page(request):
    return HttpResponse("<h1>This is SUCCESS PAGE.</h1>")

def about(reuest):
    context = {"page": "about"} # Page name
    return render(reuest, "about.html", context)

def contact(reuest):
    context = {"page": "Contact"}
    return render(reuest, "contact.html", context)