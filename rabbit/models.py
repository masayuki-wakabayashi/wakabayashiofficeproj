from django.db import models
from django.utils import timezone

class Post(models.Model):
    office_id = models.IntegerField()
    encrypted_message = models.BinaryField()
    posted_date = models.DateTimeField(default=timezone.now)