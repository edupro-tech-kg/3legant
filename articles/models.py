from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=255)
    image_url = models.URLField()  # ссылка на картинку
    link = models.URLField()  # ссылка на страницу статьи

    def __str__(self):
        return self.title
