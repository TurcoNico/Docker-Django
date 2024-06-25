from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, get_object_or_404, redirect
from .models import Fruta
from .forms import FrutaForm

def lista_frutas(request):
    frutas = Fruta.objects.all()
    return render(request, 'frutas/lista_frutas.html', {'frutas': frutas})

def detalle_fruta(request, id):
    fruta = get_object_or_404(Fruta, id=id)
    return render(request, 'frutas/detalle_fruta.html', {'fruta': fruta})

def nueva_fruta(request):
    if request.method == "POST":
        form = FrutaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_frutas')
    else:
        form = FrutaForm()
    return render(request, 'frutas/editar_fruta.html', {'form': form})

def editar_fruta(request, id):
    fruta = get_object_or_404(Fruta, id=id)
    if request.method == "POST":
        form = FrutaForm(request.POST, instance=fruta)
        if form.is_valid():
            form.save()
            return redirect('lista_frutas')
    else:
        form = FrutaForm(instance=fruta)
    return render(request, 'frutas/editar_fruta.html', {'form': form})

def eliminar_fruta(request, id):
    fruta = get_object_or_404(Fruta, id=id)
    if request.method == "POST":
        fruta.delete()
        return redirect('lista_frutas')
    return render(request, 'frutas/eliminar_fruta.html', {'fruta': fruta})
