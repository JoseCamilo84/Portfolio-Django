from django.shortcuts import render, redirect
from django.core.mail import EmailMessage
from django.contrib import messages
from django.conf import settings
from .forms import ContacForm


def portfolio(request):
    return render(request, 'portfolio.html', {})


def contac(request):
    form = ContacForm(request.POST or None)

    if form.is_valid():
        instance = form.save(commit=False)
        messages.success(request, 'Thanks for contacting me')

        subject = instance.subject
        from_email = instance.email
        # phone = instance.phone
        html_message = instance.message
        to_email = [settings.EMAIL_HOST_USER]

        email_message = EmailMessage(
            subject, html_message, from_email, to_email)
        email_message.content_subtype = 'html'
        email_message.send()

    return render(request, 'contac.html', {'form': form})


def download(request):
    return render(request, 'download.html', {})
