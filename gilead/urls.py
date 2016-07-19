from django.conf.urls import url
from gilead import views

urlpatterns = [
    url(r"^i$", views.hash_url, name = "hash_url"),
    url(r"^i(/.*)$", views.hash_redirect, name = "hash_redirect"),
]
