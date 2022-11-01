from django.shortcuts import render, redirect
from .forms import ContacForm


def portfolio(request):
    return render(request, 'portfolio.html', {})

def contac(request):
    form = ContacForm()
    return render(request, 'contac.html', { 'form': form })

def download(request):
    return render(request, 'download.html', {})

