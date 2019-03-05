from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractBaseUser


class User(AbstractBaseUser):
    username = models.CharField(max_length=100, unique=True, db_index=True)
    email = models.EmailField(max_length=120, unique=True)
    about = models.CharField(max_length=200, default='')

    USERNAME_FIELD = 'username'

    def __str__(self):
        return self.username


class Post(models.Model):
    body = models.CharField(max_length=300)
    timestamp = models.DateTimeField(db_index=True, default=timezone.now)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return 'Post {}'.format(self.body)





