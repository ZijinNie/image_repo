from django.shortcuts import render, redirect
# from core.models import Site
from image.models import Image, Comment, Like, ImageEntity
from django.contrib.auth.models import User
from .forms import ImageCreateForm, CommentCreateForm
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.conf import settings
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils.text import slugify


# image view
def show_image(request, slug):
    # site = Site.objects.first()
    image = Image.objects.get(
        Q(slug__exact=slug)
    )
    image_entity = image.imageentity_set.all()
    comments = image.comment_set.all()
    all_comments = comments
    user = image.user

    return render(request, 'image/image_detail.html', {
        # 'site': site,
        'image': image,
        'image_entity': image_entity,
        'all_comments': all_comments,
        'user': user
    })

@login_required(login_url='/user/login')
def create_image(request):
    form = ImageCreateForm()
    if request.method == 'POST':
        form = ImageCreateForm(request.POST,request.FILES)
        
        if form.is_valid():
            print('this is valid')
            image = form.save(commit=False)
            image.user = request.user
            image.slug = slugify(image.name)
            image_entity = ImageEntity(picture = form.cleaned_data.get('image_entity'), image = image)
            image.save()
            image_entity.save()
            messages.success(request, f'Your account has been created.')
            return render(request, 'user/profile.html', packBodyForProfile(request.user))
        else:
            print('not valid')
            print(form.errors)
            messages.error(request, form.errors)
            return HttpResponseRedirect(request.path_info)
    else:
        return render(request, 'image/image_new.html', {'form' : form})


def packBodyForProfile(user):
    image_objects = user.image_set.all()
    images = []
    for i , c in enumerate(image_objects):
        # print(c.imageentity_set.all())
        images.append({
            'image': c,
            'image_entity': c.imageentity_set.all()[0],
        })
    return {
        'user': user,
        'images': images
    }

@login_required(login_url='/user/login')
def create_comment(request, image_id):
    form = CommentCreateForm()
    image = Image.objects.get(id=image_id)
    if request.method == 'POST':
        form = CommentCreateForm(request.POST)
        if form.is_valid():
            print('valid')
            comment = form.save(commit=False)
            comment.author = request.user
            comment.image = image
            messages.success(request, f'Your account has been created.')
            comment.save()
            return show_image(request, image.slug)
        else:
            print(form.errors)
            messages.error(request, form.errors)
            return HttpResponseRedirect(request.path_info)
    else:
        return show_image(request, image.slug)
