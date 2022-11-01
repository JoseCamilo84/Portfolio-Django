from django import forms

class ContacForm(forms.Form):
    subject = forms.CharField(max_length=100)
    email = forms.EmailField()
    phone = forms.CharField(max_length=10)
    message = forms.CharField(widget=forms.Textarea)
