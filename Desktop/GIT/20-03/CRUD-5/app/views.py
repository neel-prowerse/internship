from django.shortcuts import render, redirect
from .forms import StoreForm
from .models import Store

# Create your views here.
def home(request):
    return render(request, 'home.html')

def store(request):
    if request.method == 'POST':
        form = StoreForm(request.POST)
        try:
            if form.is_valid():
                form.save()
                return redirect('/show')
        except:
            pass
    else:
        form = StoreForm()
    return render(request, 'index.html',{'form':form})

def show(request):
    total_price = ''
    searchTerm = request.GET.get('searchItem')
    if searchTerm:
        stores = Store.objects.order_by('-price').filter(name__icontains=searchTerm)
    else:
        stores = Store.objects.all().order_by('-price')
    total_price = sum(store.price * store.quantity for store in stores)
    return render(request, 'show.html',{'stores':stores, 'total_price':total_price,'searchTerm':searchTerm})

def edit(request, sid):
    store = Store.objects.get(sid=sid)
    return render(request, 'edit.html',{'store':store})

def update(request, sid):
    store = Store.objects.get(sid=sid)
    form = StoreForm(request.POST,instance=store)
    if form.is_valid():
        form.save()
        return redirect('/show')
    return render(request, 'edit.html',{'store':store})

def delete(request, sid):
    store = Store.objects.get(sid=sid)
    store.delete()
    return redirect('/show')