from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Student
def testing(request):
    mydata = Student.objects.all()
    template = loader.get_template('base.html')
    context = {
        'students': mydata,
    }
    return HttpResponse(template.render(context, request))
def view(request):
    students2 = Student.objects.all()
    students = request.GET.get('students')
    return render(request,'base.html',{'students':students,'students2':students2})
def home(request):
    return render(request,'home.html')