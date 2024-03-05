from django.shortcuts import render
from .models import Home
# Create your views here.
def home(request):
    if request.method == 'POST':
        model = Home()
        model.name = request.POST.get('name')
        model.number = request.POST.get('number')
        model.save()
    print("DATA STORED SUCCESSFULLY")
    return render(request,'home.html')
    