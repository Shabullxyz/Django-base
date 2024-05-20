from django.contrib import admin
from rest_framework.documentation import include_docs_urls
from django.urls import path, re_path
from . import views

urlpatterns = [
  # path("admin/", admin.site.urls),
    re_path('login/', views.login),
    re_path('register', views.register),
    re_path('profile', views.profile),
  # path("docs/",include_docs_urls(title="login API"))
]