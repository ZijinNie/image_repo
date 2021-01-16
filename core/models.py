from django.db import models
from django.contrib.auth.models import User

class Site(models.Model):
    name = models.CharField(max_length=255)
    logo = models.ImageField(upload_to='site/logo/', blank=True)

    class Meta:
        verbose_name = "Site"
        verbose_name_plural = "Site"



