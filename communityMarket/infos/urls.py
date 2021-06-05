from django.urls import path

from . import views

urlpatterns = [
    path("", views.main, name='main'),
    path("form", views.form_page, name="form-page"),
]