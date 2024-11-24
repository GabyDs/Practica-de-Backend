# from django.shortcuts import render

# Django uses request and response objects to pass state through the system
from django.http import HttpResponse, JsonResponse

import json

# Then Django loads the appropriate view, passing the HttpRequest as the first argument to the view function
def index(request):
    return HttpResponse("Hello, world. You're at the two endpoints index.")

def user(request):
    res = {"user":"user"}
    # default: "content_type", "application/json"
    return JsonResponse(res)

def admin(request):
    res = {"user":"admin"}
    return JsonResponse(res)