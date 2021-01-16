from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model, logout, login, authenticate
from django.contrib.auth.models import User
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import EmailMessage
from django.contrib.auth.decorators import login_required
from django.db.models import Q
# from core.models import Site
from django.contrib import messages
from core.forms import UserRegistrationForm, UserLoginForm, ProfileUpdateForm
from django.http import HttpResponseRedirect, HttpResponse

UserModel = get_user_model()


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            # current_site = get_current_site(request)
            # mail_subject = 'Activate your account.'
            # message = render_to_string('user/account_activate_email.html', {
            #     'user': user,
            #     'domain': current_site.domain,
            #     'uid': urlsafe_base64_encode(force_bytes(user.pk)),
            #     'token': default_token_generator.make_token(user),
            # })
            # to_email = form.cleaned_data.get('email')
            # email = EmailMessage(
            #     mail_subject, message, to=[to_email]
            # )
            # email.send()
            # messages.success(request, 'Please confirm your email address to complete the registration')
            messages.success(request, f'Your account has been created.')
            return render(request, 'user/login.html')
        else:
            messages.error(request, form.errors)
            return HttpResponseRedirect(request.path_info)
    else:
        # site = Site.objects.first()
        form = UserRegistrationForm()
        return render(request, 'user/register.html', {
            # 'site': site,
            'form': form
        })


def activate(request, uidb64, token):
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user = UserModel._default_manager.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and default_token_generator.check_token(user, token):
        user.is_active = True
        user.save()
        return HttpResponse('Thank you for your email confirmation. Now you can login your account.')
    else:
        return HttpResponse('Activation link is invalid!')


def login_view(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, 'You have logged in.')
                return HttpResponseRedirect('/')
            else:
                messages.error(request,
                               'Sorry, something went wrong. Please make sure the username and password are correct.')
                return HttpResponseRedirect(request.path_info)
    else:
        # site = Site.objects.first()
        form = UserLoginForm()
        return render(request, 'user/login.html', {
            # 'site': site,
            'form': form
        })


def logout_view(request):
    logout(request)
    # site = Site.objects.first()
    return render(request, 'user/logout.html', {
        # 'site': site,
    })


@login_required(login_url='/user/login')
def profile(request, username):
    # site = Site.objects.first()
    user = User.objects.filter(Q(username__exact=username)).all()[0]
    user_profile = user.profile
    # user = request.user

    image_objects = user.image_set.all()
    images = []
    for i , c in enumerate(image_objects):
        # print(c.imageentity_set.all())
        images.append({
            'image': c,
            'image_entity': c.imageentity_set.all()[0],
        })

    if request.method == 'POST':
        form = ProfileUpdateForm(request.POST, request.FILES)
        if request.user.is_authenticated:
            if form.is_valid():
                user.email = form.cleaned_data['email']
                # user_profile.phone = form.cleaned_data['phone']
                user.first_name = form.cleaned_data['first_name']
                user.last_name = form.cleaned_data['last_name']
                user_profile.image = form.cleaned_data['image']
                user.save()
                user_profile.save()
                messages.success(request, 'Your profile has been updated.')
                return HttpResponseRedirect(request.path_info)
            else:
                messages.error(request, form.errors)
                return HttpResponseRedirect(request.path_info)
    else:
        form = ProfileUpdateForm()

    return render(request, 'user/profile.html', {
        # 'site': site,
        'form': form,
        'user': user,
        'images': images
        # 'reviews': reviews,
        # 'approved_apartments': approved_apartments,
        # 'apartment_requests': apartment_requests
    })
