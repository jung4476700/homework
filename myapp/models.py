from django.db import models

# Create your models here.
class Board(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    update_date = models.DateTimeField(auto_now=True)
    video_key=models.CharField(max_length=50, null=True)
    
    def __str__(self):
        return self.title
    
    def summary(self):
        return self.body[:50]