from django.db import models
from django.contrib.auth.models import User 
from django.utils import timezone

# Create your models here.

class Blog(models.Model):
    user_id = models.ForeignKey(User,on_delete=models.CASCADE)
    title = models.CharField(max_length=150)
    description = models.TextField(max_length=500)
    date_created = models.DateTimeField(default=timezone.now)
    
    # date_created = models.DateTimeField(default=datetime.timezone)

    def __str__(self):
        return self.title

  