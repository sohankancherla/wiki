from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("search/", views.search, name="search"),
    path("new-page", views.new, name="new-page"),
    path("add-page", views.add, name="add-page"),
    path("edit-page", views.edit, name="edit-page"),
    path("<str:name>", views.entry, name="entry")
]
