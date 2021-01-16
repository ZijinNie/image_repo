from django.db import models
from django.contrib.auth.models import User

# Apartment abstract model. extend to AptRequest and AptApproved
class Image(models.Model):
    # Basic Info
    name = models.CharField(max_length=255, blank=True)
    slug = models.SlugField(unique=True)
    created_time = models.DateTimeField(auto_now=True)
    description = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)


# Image entity.
class ImageEntity(models.Model):
    picture = models.ImageField(upload_to='image/', blank=True, max_length=500)
    image = models.ForeignKey(Image, on_delete=models.CASCADE)
    class Meta:
        verbose_name = "Image picture"
        verbose_name_plural = "Image pictures"

class Like(models.Model):
    # Basic Info
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ForeignKey(Image, on_delete=models.CASCADE)

# User reviews
class Comment(models.Model):
    content = models.TextField(blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ForeignKey(Image, on_delete=models.CASCADE)
    created_time = models.DateTimeField(auto_now=True)
    def __str__(self):
        return 'Comment by %s on %s' % (self.author.username, self.created_time)

    class Meta:
        verbose_name = "Comment"
        verbose_name_plural = "Comments"

class Like(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ForeignKey(Image, on_delete=models.CASCADE)
    created_time = models.DateTimeField(auto_now=True)

