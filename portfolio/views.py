from django.shortcuts import render, redirect
from django.core.mail import EmailMessage
from django.contrib import messages
from .forms import ContacForm


def portfolio(request):
    return render(request, 'portfolio.html', {})


def contac(request):
    form = ContacForm(request.POST or None)
    instance = form.save(commit=False)
    if form.is_valid():
        subject = [instance.subject]
        email = [instance.email]
        phone = [instance.phone]
        message = [instance.message]

        email_message = EmailMessage(subject, email, phone, message)
        email_message.content_subtype = 'html'
        email_message.send()
        messages.success(request, 'Gracias por contactarte conmigo')

    return render(request, 'contac.html', {'form': form})


def download(request):
    return render(request, 'download.html', {})

