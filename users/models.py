from django.contrib.auth.models import AbstractUser
from django.db import models

# TODO раскомментировать "email = models.EmailField(unique=True)"


class User(AbstractUser):
    bio = models.TextField(
        verbose_name='Биография',
        blank=True,
    )
    # email = models.EmailField(unique=True)


class Template(models.Model):
    name = models.CharField(null=True, max_length=256)
    user = models.ForeignKey(User,
                             related_name='templates',
                             on_delete=models.CASCADE,
                             default=1)
    text = models.TextField(null=True)

    class Meta:
        verbose_name = 'Шаблон'
        verbose_name_plural = 'Шаблоны'
        ordering = ['user']

    def __str__(self):
        return self.text[:10]

