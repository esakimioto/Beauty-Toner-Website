from django.shortcuts import render
from django.http import HttpResponse
from .models import purchase
from .forms import PurchaseForm

def index(request):
    return render(request, "Beauty Products.html")


# Create your views here.
def form(request):
    print("aaa")
    form = PurchaseForm(request.POST)
    return render(request, "forms.html", {
        'form': form
    })

def index2(request):
    if request.method == 'POST':
        form = PurchaseForm(request.POST)
        if form.is_valid():
            model = purchase()
            model.period = form.cleaned_data['period']
            model.prefectures = form.cleaned_data['prefectures']
            model.municipalities = form.cleaned_data['municipalities']
            model.name1 = form.cleaned_data['name1']
            model.name2 = form.cleaned_data['name2']
            model.phone_number = form.cleaned_data['phone_number']
            model.email_address = form.cleaned_data['email_address']
            model.arrival_date = form.cleaned_data['arrival_date']
            model.save()

    return HttpResponse("Hello, world. You're at the index2 index.")
    
