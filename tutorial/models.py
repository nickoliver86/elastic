from django.db import models
from datetime import date
from datetime import datetime

# Create your models here.

class Note(models.Model):
    text = models.TextField(max_length=200)
    author = models.TextField(max_length=200)
    pub_date = models.DateTimeField()
