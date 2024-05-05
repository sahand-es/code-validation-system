from django.urls import path
from . import views


urlpatterns = [
    path("", views.code_page)
    #     todo: something like google meet codes
]
