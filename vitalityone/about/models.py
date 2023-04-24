from django.db import models
from django.utils import timezone


# Create your models here.

class Contact(models.Model):
    contact_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=100)
    message = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return 'Message from ' + self.name + ' - ' + self.email
    
