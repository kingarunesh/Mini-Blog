from django.urls import path

from dashboard.views import sign_up


urlpatterns = [
    path("sign-up/", view=sign_up, name="sign_up")
]
