

from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render, render_to_response
from django.utils import simplejson
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_GET, require_POST
from webapp.emailer import send_email, send_template_email
from webapp.forms import Create_Friendship, Create_Wall_post, Edit_User, LoginForm, ShortSignupForm
from webapp.models import Friendship, User, Wall_post
from webapp.utils import JsonResponse


@require_POST
def login(request):
    """
    Handles the login action.
    """
    form = LoginForm(None, data=request.POST)
    if form.is_valid():
        auth_login(request, form.get_user())
        return JsonResponse(data={'redirect_to': reverse('webapp.pages.user_profile', args=(request.user.id, ))})

    return JsonResponse(errors=form.errors)


@require_POST
def sign_up(request):
    """Create a User object"""
    form = ShortSignupForm(request.POST)
    if form.is_valid():
        user = form.save()
        user = authenticate(username=request.POST['email'],
                            password=request.POST['password'])
        auth_login(request, user)

        redirect_url = reverse('webapp.pages.edit_profile')
        return JsonResponse(data={'redirect_to': redirect_url})

    return JsonResponse(errors=form.errors)


@require_POST
def create_wall_post(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    form = Create_Wall_post(request.POST)
    if form.is_valid():
        wall_post = form.save(commit=False)

        # set foreign keys
        wall_post.writer = request.user
        wall_post.wall_owner = user

        wall_post.save()  # persist the object to the DB

        redirect_url = reverse('webapp.pages.homepage')
        return JsonResponse(data={'redirect_to': redirect_url})

    return JsonResponse(errors=form.errors)


@require_POST
def create_friendship(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    form = Create_Friendship(request.POST)
    if form.is_valid():
        friendship = form.save(commit=False)

        # set foreign keys
        friendship.requester = request.user
        friendship.accepter = user

        friendship.save()  # persist the object to the DB

        redirect_url = reverse(
            'webapp.pages.friendship_page', args=(friendship.id, ))
        return JsonResponse(data={'redirect_to': redirect_url})

    return JsonResponse(errors=form.errors)


@require_POST
def edit_user(request):
    form = Edit_User(request.POST, instance=request.user)
    if form.is_valid():
        user = form.save()

        redirect_url = reverse('webapp.pages.user_profile', args=(user.id, ))
        return JsonResponse(data={'redirect_to': redirect_url})

    return JsonResponse(errors=form.errors)
