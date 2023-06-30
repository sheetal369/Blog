from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from accounts.models import CustomUser
from django.urls import reverse


class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status=Post.Status.PUBLISHED)


class Post(models.Model):
    class Status(models.TextChoices):
        DRAFT = "DF", "Draft"
        PUBLISHED = "PB", "Published"

    title = models.CharField(
        max_length=200
    )  # Fields are displayed a/c to declaration order
    slug = models.SlugField(max_length=300, unique_for_date="publish")
    body = models.TextField(max_length=500)

    publish = models.DateTimeField(
        default=timezone.now
    )  # if not set explicitly, current datetime is set
    created = models.DateTimeField(auto_now_add=True)  # Sets when the obj is first created
    updated = models.DateTimeField(auto_now=True)  # Updates the field everytime, it is saved or updated

    status = models.CharField(max_length=2, default=Status.DRAFT, choices=Status.choices )
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="my_blogs")

    objects = models.Manager()  # The default manager
    published = PublishedManager()  # Our custom manager.

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["-publish"]
        indexes = [models.Index(fields=["-publish"])]
        db_table = "Post"  # Default Table name : mysite_blog

    def get_absolute_url(self):
        return reverse(
            "blog:post_detail",
            args=[self.publish.year, self.publish.month, self.publish.day, self.slug],
        )
