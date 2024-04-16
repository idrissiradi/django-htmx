from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.views.decorators.http import require_GET, require_POST
from django_htmx.middleware import HtmxDetails


class HtmxHttpRequest(HttpRequest):
    htmx: HtmxDetails


@require_GET
def index(request: HtmxHttpRequest) -> HttpResponse:
    return render(request, "home.html")


@require_POST
def index_post(request: HtmxHttpRequest) -> HttpResponse:
    email = request.POST.get("email")
    return render(request, "home.html#test-partial", {"email": email})
