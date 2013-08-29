

from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render, render_to_response
from django.utils import simplejson
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_GET, require_POST
from webapp.models import User
from webapp.utils import get_results


@require_GET
def homepage(request):
    page_context = {}

    return render(request, "homepage.html", page_context)


@require_GET
def user_profile(request, user_id):
    page_context = {}
    page_context['user'] = get_object_or_404(User, pk=user_id)

    return render(request, "user_profile.html", page_context)


@require_GET
def edit_profile(request):
    page_context = {}

    return render(request, "edit_profile.html", page_context)


@require_GET
def all_users(request):
    page_context = {}

    page_context['users'] = User.objects.exclude(
        username='admin').order_by('-date_joined')

    return render(request, "all_users.html", page_context)
