from django.db import models

from django.forms import fields, widgets
# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    createdOn = models.DateTimeField(auto_now_add=True)
    lastEdited = models.DateTimeField(auto_now=True)
    game = models.TextField()
    platform = models.TextField()
    body = models.TextField()
    tags = models.TextField()
    author = models.TextField()
    # author needs to be added
    class Meta:
        ordering = ['-createdOn']  # newest posts first
    def __str__(self):
        return self.description
    
        
    def create_post (self, title, description, created_on, 
                     last_edited, game, platform,
                     body, tags, author):
        if not title:
            raise ValueError('Must provide a title')
        
        if not description:
            raise ValueError('Must provide a description')
        
        if not game:
            raise ValueError('Must provide a game')
        
        if not platform:
            raise ValueError('Must provide a platform')
        
        if not body:
            raise ValueError('Must provide a body')
        
        if not tags:
            raise ValueError('Must provide tags')
        
        post_obj = self.model(
            title = self.normalize_title(title),   
        )
        
        post_obj.title = title
        post_obj.description = description
        post_obj.createdOn = created_on
        post_obj.last_edited = last_edited
        post_obj.game = game
        post_obj.platform = platform
        post_obj.body = body
        post_obj.tags = tags
        post_obj.author = author
        
        post_obj.save(using=self._db)
        return post_obj
        
    def __str__(self):
        return self.title
