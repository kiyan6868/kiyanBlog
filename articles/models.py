from django.db import models


class Articles(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField()
    body = models.TextField()
    publish_date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(default='default.jpg', blank=True)

    def __str__(self):
        return self.title

    def snippet(self):
        if len(self.body) > 100:
            return self.body[0:100] + '...'
        return self.body

