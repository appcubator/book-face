

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
