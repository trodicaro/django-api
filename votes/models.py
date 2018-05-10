from django.db import models
from django.utils import timezone

# Create your models here.

class Vote(models.Model):
    subject = models.CharField(blank = False, max_length = 255)
    vote_taken = models.DateTimeField(blank = False, default = timezone.now)
    ayes = models.IntegerField(default = 0)
    nays = models.IntegerField(default = 0)

