from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *

# Create your views here.

def receipes(request):
    if request.method == "POST":
        data = request.POST
        receipe_name = data.get("receipe_name")
        receipe_description = data.get("receipe_decription")
        receipe_image = request.FILES.get("receipe_image") # For file upload feild

        Receipe.objects.create(
            receipe_name = receipe_name,
            receipe_decription = receipe_description,
            receipe_image = receipe_image
        )

        return redirect("/receipes/")
    
    queryset = Receipe.objects.all()
    context = {"receipe": queryset}
        
    return render(request, "receipes.html", context)


def update_receipe(request, id):
    queryset = Receipe.objects.get(id = id)
    if request.method == "POST":
        data = request.POST
        receipe_name_updated = data.get("receipe_name")
        receipe_description_updated = data.get("receipe_decription")
        receipe_image_updated = request.FILES.get("receipe_image") # For file upload feild

        queryset.receipe_name = receipe_name_updated
        queryset.receipe_decription = receipe_description_updated

        if receipe_image_updated:
            queryset.receipe_image = receipe_image_updated
        queryset.save()
        return redirect("/receipes/")

    context = {"receipes": queryset}
    return render(request, "update_receipes.html", context)


def delete_receipe(request, id):
    queryset = Receipe.objects.get(id = id)
    queryset.delete()
    return redirect("/receipes/")