from django.contrib import admin
from image.models import *

admin.site.register(Image)
admin.site.register(ImageEntity)
admin.site.register(Comment)
admin.site.register(Like)
