
from ckeditor.fields import RichTextField
from django.urls import reverse
from unicodedata import category
from django.utils.text import slugify
from django.db import models
from django.contrib.auth import get_user_model

STATUS = ((0, "Draft"), (1, "Publish"))

User = get_user_model()


class Categories(models.Model):
    name = models.CharField(max_length=20, unique=True)

    def __str__(self) -> str:
        return self.name

    class Meta:
        ordering = ['id']


class Post(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(
        Categories, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=100, blank=True,)
    description = RichTextField(blank=True)
    slug = models.SlugField(unique=True, null=True, blank=True)
    owner = models.ForeignKey(
        User, related_name='posts', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='media', null=True, blank=True)
    status = models.IntegerField(
        choices=STATUS, default=0, blank=True, null=True)

    def __str__(self) -> str:
        return self.title

    def get_absolute_url(self):
        return reverse("post_detail", kwargs={"slug": self.slug})

    class Meta:
        ordering = ['-created']

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title[:50])
        super(Post, self).save(*args, **kwargs)


class SliderPost(models.Model):
    created = models.DateTimeField(auto_now_add=True,)
    title = models.CharField(max_length=100, blank=True, default='')
    description = models.TextField(blank=True, default='')
    image = models.ImageField(upload_to='media')
    slug = models.SlugField(unique=True, null=True, blank=True)

    def __str__(self) -> str:
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title[:50])
        super(SliderPost, self).save(*args, **kwargs)


# class AdminPost(Post):
#     def __init__(self,):
#         self.status = models.IntegerField(
#             choices=STATUS, default=1, blank=True, null=True)
#         self.language = models.DateField()


class Comment(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    body = models.TextField(blank=False)
    owner = models.ForeignKey(
        User, related_name='comments', on_delete=models.CASCADE)
    post = models.ForeignKey(
        Post, related_name='comments', on_delete=models.CASCADE)

    class Meta:
        ordering = ['created']

    def __str__(self):
        return "Comment {} by {}".format(self.body, self.body)


class NewsLetterEmail(models.Model):
    email = models.EmailField()

    def __str__(self):
        return self.email


class Description(models.Model):
    description = RichTextField()


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='profile_pictures')

    def __str__(self):
      return f'{self.user.first_name} Profile'
