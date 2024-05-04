from django.urls import path
from . import views


urlpatterns = [
    path("", views.load_page)
    #     todo: something like google meet codes
]
