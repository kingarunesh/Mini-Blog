from django.urls import path

from index.views import index


urlpatterns = [
    path("", view=index, name="index")
]