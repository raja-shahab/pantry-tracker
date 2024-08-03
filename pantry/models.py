from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Pantry(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    inventory_name = models.CharField(max_length=100)
    inventory_count = models.IntegerField()
    inventory_description = models.TextField()
    inventory_image = models.ImageField(upload_to="inventory_images")
    inventory_view_count = models.PositiveIntegerField(default=1)
