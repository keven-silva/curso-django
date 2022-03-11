from django.db import models
from django.db.models.fields import BooleanField

# Create your models here.
class Todo(models.Model):
    name = models.CharField(max_length=120)
    done = BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)