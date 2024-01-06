from django.urls import path

from dashboard.views import sign_up, login_view, dashboard, logout_view


urlpatterns = [
    path("sign-up/", view=sign_up, name="sign_up"),
    path("login/", view=login_view, name="login_view"),
    path("dashboard/", view=dashboard, name="dashboard"),
    path("logout/", view=logout_view, name="logout_view")
]
