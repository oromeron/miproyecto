from django.shortcuts import render

def presentacion(request):
    return render(request, 'base.html')

def visualizar(request):
    return render(request, 'base.html')