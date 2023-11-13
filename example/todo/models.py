from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Task(models.Model):
    title=models.CharField('Название', max_length=50, blank=True, null=True)
    task=models.TextField('Описание', blank=True, null=True)

    def __str__(self):
        return f"{self.title} {self.task}"

    class Meta:
        verbose_name='Задача'
        verbose_name_plural='Задачи'

# Категории
class Tags(models.Model):
    tags=models.TextField('Категория', null=True, blank=True)

    def __str__(self):
        return f"{self.tags}"

    def to_json(self):
        return {
            'tags': self.tags,

        }
    class Meta:
        verbose_name='Категория'
        verbose_name_plural='Категории'

class Post(models.Model):
    title = models.CharField('Название', max_length=50, blank=True, null=True)
    post = models.TextField('Описание', blank=True, null=True)
    date_of_staging = models.DateTimeField('Дата создания', auto_now_add=True, null=True, blank=True) #null=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, verbose_name='Создатель')
    image = models.ImageField('Изображение', null=True, upload_to='images/', blank=True)
    tags = models.ForeignKey(Tags, verbose_name='Категории', on_delete=models.CASCADE, null=True, blank=True,)

    def __str__(self):
        return f"{self.title} {self.post} {self.date_of_staging} {self.author} {self.image}"

    # def save(self, *args, **kwargs):
    #     print("Saving post...")

        # super(Task, self).save(*args, **kwargs)
        # print("Post saved.")

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'

class Image(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='images', null=True, verbose_name='Пост',)
    image = models.ImageField('Изображение', null=True, upload_to='images/', blank=True)
