from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=100)
    subheading = models.CharField(max_length=200, blank=True, null=True)  # Add this line
    topics = models.CharField(max_length=100)
    cont = models.TextField()
    image = models.ImageField(upload_to='blog/images/', blank=True, null=True)
