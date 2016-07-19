import os
from django.http import HttpResponse
from django.shortcuts import redirect, render

i_static = os.path.join(os.path.dirname(os.path.abspath(__file__)),
        "static", "i_base.html")
with open(i_static, "r") as i_file:
    I_HTML = i_file.read()

def hash_url (request):
    if request.method == "POST":
        if len(request.POST) == 1 and "url" in request.POST:
            return HttpResponse("js page")
    return HttpResponse(I_HTML)

def hash_redirect (request):
    pass
