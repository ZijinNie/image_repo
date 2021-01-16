from django.shortcuts import render, redirect
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from image.models import Image
from django.conf import settings
from core.models import *
from image.models import Image
from django.contrib import messages


# Create your views here.
# home view
def home(request):
    # site = Site.objects.first()
    image_objects = Image.objects.order_by('-id')[0:20]
    # print(image_objects)
    images = []
    for i , c in enumerate(image_objects):
        # print(c.imageentity_set.all())
        images.append({
            'image': c,
            'image_entity': c.imageentity_set.all()[0],
            'author': c.user
        })
    return render(request, 'index.html', {
        # 'site': site
        'images': images,
    })


# search view
def browse_search(request):
    # site = Site.objects.first()
    query = request.GET.get('q', '')
    if query:
        image_list = Image.objects.filter(
            Q(name__icontains=query)
        )
    else:
        image_list = []

    image_list_with_pic = []
    for i , c in enumerate(image_list):
        # print(c.imageentity_set.all())
        image_list_with_pic.append({
            'image': c,
            'image_entity': c.imageentity_set.all()[0],
        })
    page = request.GET.get('page', 1)
    paginator = Paginator(image_list_with_pic, settings.ENTRY_PER_PAGE)
    try:
        images = paginator.page(page)
    except PageNotAnInteger:
        images = paginator.page(1)
    except EmptyPage:
        imges = paginator.page(paginator.num_pages)

    return render(request, 'image/image_search.html', {
        # 'site': site,
        'images': images,
        'q': query
    })


