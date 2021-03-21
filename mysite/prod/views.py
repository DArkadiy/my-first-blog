from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Zakaz, Detal
from .forms import ZakazForm, DetalForm


# Create your views here.
def zakaz_list(request):
    zakazs = Zakaz.objects.filter()
    return render(request, 'prod/zakaz_list.html', {'zakazs': zakazs})

def zakaz_detail(request, pk):
    zakaz = get_object_or_404(Zakaz, pk=pk)
    return render(request, 'prod/zakaz_detail.html', {'zakaz': zakaz})

def zakaz_new(request):
    if request.method == "POST":
        form = ZakazForm(request.POST)
        if form.is_valid():
            zakaz = form.save(commit=False)
            zakaz.author = request.user
            zakaz.created_date = timezone.now()
            zakaz.save()
            return redirect('zakaz_detail', pk=zakaz.pk)
    else:
        form = ZakazForm()
    return render(request, 'prod/zakaz_add.html', {'form': form})

def zakaz_edit(request, pk):
    zakaz = get_object_or_404(Zakaz, pk=pk)
    if request.method == "POST":
        form = ZakazForm(request.POST, instance=zakaz)
        if form.is_valid():
            zakaz = form.save(commit=False)
            zakaz.author = request.user
            zakaz.created_date = timezone.now()
            zakaz.save()
            return redirect('zakaz_detail', pk=zakaz.pk)
    else:
        form = ZakazForm(instance=zakaz)
    return render(request, 'prod/zakaz_edit.html', {'form': form})



def detal_list(request):
    detals = Detal.objects.filter()
    return render(request, 'prod/detal_list.html', {'detals': detals})

def detal_detail(request, pk):
    detal = get_object_or_404(Detal, pk=pk)
    return render(request, 'prod/detal_detail.html', {'detal': detal})

def detal_new(request):
    if request.method == "POST":
        form = DetalForm(request.POST)
        if form.is_valid():
            detal = form.save(commit=False)
            detal.author = request.user
            detal.created_date = timezone.now()
            detal.save()
            return redirect('detal_detail', pk=detal.pk)
    else:
        form = DetalForm()
    return render(request, 'prod/detal_add.html', {'form': form})

def detal_edit(request, pk):
    detal = get_object_or_404(Detal, pk=pk)
    if request.method == "POST":
        form = DetalForm(request.POST, instance=detal)
        if form.is_valid():
            detal = form.save(commit=False)
            detal.author = request.user
            detal.created_date = timezone.now()
            detal.save()
            return redirect('detal_detail', pk=detal.pk)
    else:
        form = DetalForm(instance=detal)
    return render(request, 'prod/detal_edit.html', {'form': form})