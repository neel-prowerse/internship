from django.shortcuts import render
from .tasks import add, mul
def calculate(request):
    add_result  = add.delay(4, 4)
    mul_result = mul.delay(4, 4)
    return render(request, 'result.html',{ 'add_result':add_result.get(), 'mul_result':mul_result.get()})
