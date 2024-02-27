from django.shortcuts import render
# from django.http import HttpResponse
from  .models import News
# Create your views here.
def home(request):
    newss = News.objects.all()
    return render(request,'home.html',{'newss':newss})