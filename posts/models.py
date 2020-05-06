# from django.contrib.auth.models import User
from django.utils import timezone
from django.conf import settings
from django.db import models


User = settings.AUTH_USER_MODEL
# Create your models here.


class PostManager(models.Manager):
    def published(self):
        now = timezone.now()
        return self.get_queryset().filter(published_date__lte=now)


class Post(models.Model):
    # to get all posts of an user we can use u.post_set.all() where u is user instance
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    content = models.TextField()
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, auto_now_add=False)
    published_date = models.DateTimeField(
        auto_now=False, auto_now_add=False, null=True, blank=True)

    objects = PostManager()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        print(self)
        return f"/posts/{self.id}"

    class Meta:
        ordering = ['-published_date', '-updated_at', '-created_at']
