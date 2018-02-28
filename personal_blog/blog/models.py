from django.db import models
from django.utils import timezone

class Post(models.Model):
    author = models.ForeignKey('auth.user',on_delete = models.CASCADE)
    title = models.CharField(max_length = 300)
    text = models.TextField()
    start_date = models.DateTimeField(default = timezone.now)
    published_date = models.DateTimeField(null = True,blank =True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
