from django.db import models
from datetime import datetime

from  ckeditor.fields import RichTextField


class Post(models.Model):
    title = models.CharField(max_length=200)
    text = RichTextField()
    created_at = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Post"
        verbose_name_plural = "Posts"

# Create your models here.
