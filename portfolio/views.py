from django.shortcuts import render, redirect
from django.core.mail import EmailMessage
from django.contrib import messages
from django.template.loader import render_to_string
from django.conf import settings
from .forms import ContacForm


def portfolio(request):
    return render(request, 'portfolio.html', {})


def contac(request):
    form = ContacForm(request.POST or None)

    if form.is_valid():
        instance = form.save(commit=False)
        # instance.save()

        subject = instance.subject
        from_email = instance.email
        to_email = [settings.EMAIL_HOST_USER]
        phone = instance.phone
        html_template = render_to_string('layouts/parcels/email.html', {
            'phone': phone,
            'email': from_email,
            'message': instance.message
        })

        # html_template = instance.message

        email_message = EmailMessage(
            subject,
            html_template,
            from_email,
            to_email
        )

        email_message.fail_silently = False
        email_message.content_subtype = 'html'
        email_message.send()

        messages.success(request, 'Thanks for contacting me')

    return render(request, 'contac.html', {'form': form})


def download(request):
    return render(request, 'download.html', {})
