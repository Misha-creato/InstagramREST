from django.db import models
from settings.base import AUTH_USER_MODEL as UserModel
from profiles.models import Profile


class Post(models.Model):
    author = models.ForeignKey(
        to=Profile,
        on_delete=models.CASCADE,
        related_name='posts'
    )
    description = models.TextField(
        verbose_name='Description',
        blank=False
    )
    created_at = models.DateTimeField(
        verbose_name='Created_at',
        auto_now=True
    )
    

class Photo(models.Model):
    photo = models.ImageField(
        verbose_name='Photo',
        upload_to='photos',
        null=False,
        blank=False,
    )
    post = models.ForeignKey(
        to=Post,
        on_delete=models.CASCADE,
        related_name='photos'
    )


class Like(models.Model):
    user = models.ForeignKey(
        to=UserModel,
        on_delete=models.CASCADE,
        related_name='likes'
    )
    post = models.ForeignKey(
        to=Post,
        on_delete=models.CASCADE,
        related_name='likes'
    )


class Comment(models.Model):
    user = models.ForeignKey(
        to=UserModel,
        on_delete=models.CASCADE,
        related_name='comments'
    )
    post = models.ForeignKey(
        to=Post,
        on_delete=models.CASCADE,
        related_name='comments'
    )
    comment = models.TextField(
        verbose_name='Comment',
        max_length=300
    )
    created_at = models.DateTimeField(
        verbose_name='Created_at',
        auto_now=True
    )
    