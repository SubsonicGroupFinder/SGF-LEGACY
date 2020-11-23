from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    createdOn = models.DateTimeField(auto_now_add=True)
    lastEdited = models.DateTimeField(auto_now=True)
    # author needs to be added

    def __str__(self):
        return self.title
