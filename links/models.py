from django.db import models

# Create your models here.


class Link(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    url = models.URLField(max_length=200)
    created_at = models.DateTimeField(auto_now=False, auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True, auto_now_add=False)


    def __str__(self):
        return self.name