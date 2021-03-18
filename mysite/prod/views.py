from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Zakaz
from .forms import ZakazForm


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
    return render(request, 'prod/zakaz_edit.html', {'form': form})

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
