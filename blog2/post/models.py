from django.conf import settings
from django.db import models


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    # Указываем, что будет передаваться при выводе экземпляра класса Post, вместо "Post(0)"
    def __str__(self) -> str:
        return self.title
