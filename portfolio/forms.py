from django.forms import ModelForm
from .models import MessageUser


class ContacForm(ModelForm):
    class Meta:
        model = MessageUser
        fields = [
            'subject',
            'email',
            'phone',
            'message'
        ]
