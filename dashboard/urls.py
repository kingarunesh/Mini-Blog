from django.urls import path

from dashboard.views import sign_up, login_view, logout_view, dashboard, edit_profile_view, change_password_view, blogs_view


urlpatterns = [
    path("sign-up/", view=sign_up, name="sign_up"),
    path("login/", view=login_view, name="login_view"),
    path("logout/", view=logout_view, name="logout_view"),
    
    path("dashboard/", view=dashboard, name="dashboard"),
    path("dashboard/edit-profile/", view=edit_profile_view, name="edit_profile_view"),
    path("dashboard/change-password/", view=change_password_view, name="change_password_view"),
    path("dashboard/blogs/", view=blogs_view, name="blogs_view"),
]
