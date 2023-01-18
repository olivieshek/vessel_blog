from datetime import datetime
from django.db import models
from autoslug import AutoSlugField
from django.contrib.auth.models import User


# class AuthorUser(User):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#
#     def __str__(self):
#         return self.user.username


class ModelCategory(models.Model):
    name = models.CharField(max_length=30, verbose_name="Название категории", unique=True)
    slug = AutoSlugField(populate_from="name", unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name_plural = "Categories"

    def __str__(self):
        return str(self.name)


# TODO default datetime
class Post(models.Model):
    title = models.CharField(max_length=100, verbose_name="Заголовок")
    body = models.TextField(max_length=1000, verbose_name="Основной текст")
    summary = ''
    image = models.ImageField(upload_to="blog/images/", default="", verbose_name="Фотография к посту")
    date = models.DateField(verbose_name="Дата публикации", default=datetime.now)
    time = models.TimeField(verbose_name="Время публикации")
    author = models.ForeignKey(
        User,
        verbose_name="User",
        related_name="posts",
        on_delete=models.CASCADE,
        default=123
    )
    category = models.ForeignKey(
        to=ModelCategory,
        related_name="posts",
        on_delete=models.SET_NULL,
        blank=True,
        null=True
    )

    def __str__(self):
        return f'''"{self.title}" --- {self.date}'''



