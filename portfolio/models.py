from django.db import models


class MessageUser(models.Model):
    subject = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=10)
    message = models.TextField()
