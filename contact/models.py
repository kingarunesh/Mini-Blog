from django.db import models


class Contact(models.Model):
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    email = models.EmailField(max_length=250)
    phone = models.CharField(max_length=12)
    subject = models.CharField(max_length=100)
    message = models.TextField()
    send_date = models.DateTimeField(auto_now_add=True)