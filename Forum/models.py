from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
#Each class is a table in DB
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    files = models.FileField(upload_to='docs', null=True, blank=True)
    date_posted = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})

class Reply(models.Model):
    post = models.ForeignKey(Post, related_name="reply", on_delete=models.CASCADE)
    author = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%s -%s' % (self.post.title, self.author)

    def get_absolute_url(self):
        return reverse('forum-home')