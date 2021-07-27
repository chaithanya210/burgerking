from django.shortcuts import render
from .models import booking_table,contact_table
def index(request):
    return render(request,"index.html")
def contact(request):
    return render(request,"contact.html")
def booking(request):
    return render(request,"booking.html")
def booking_save(request):
    obj1=booking_table()
    obj1.name=request.POST.get("name")
    obj1.email=request.POST.get("email")
    obj1.mobile=request.POST.get("mobile")
    obj1.date=request.POST.get("date")
    obj1.time=request.POST.get("time")
    obj1.save()
    return render(request,"index.html")
def contact_save(request):
    obj2=contact_table()
    obj2.cname=request.POST.get("cname")
    obj2.cemail=request.POST.get("cemail")
    obj2.subject=request.POST.get("subject")
    obj2.message=request.POST.get("message")
    obj2.save()
    return render(request,"index.html")
def about(request):
    return render(request,"about.html")
def feature(request):
    return render(request,"feature.html")
def team(request):
    return render(request,"team.html")
def menu(request):
    return render(request,"menu.html")






# Create your views here.
