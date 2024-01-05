from django.db import models


class Blog(models.Model):
    title = models.CharField(max_length=250)
    description = models.TextField()
    create_date = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)