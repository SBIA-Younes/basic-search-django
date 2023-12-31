from django.db import models


class BlogPost(models.Model):
  
  title = models.CharField(max_length=255)
  content = models.TextField()
  
  class Meta:
    verbose_name = "Blog"
    
  def __str__(self):
    return self.title