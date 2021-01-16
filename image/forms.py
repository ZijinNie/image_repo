from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from image.models import Image, Comment

class ImageCreateForm(forms.ModelForm):
    image_entity = forms.ImageField(label='image')
    name = forms.CharField()
    description = forms.CharField()
    class Meta:
        model = Image
        fields = ['image_entity', 'name', 'description']

class CommentCreateForm(forms.ModelForm):
    content = forms.CharField()
    class Meta:
        model = Comment
        fields = ['content']

