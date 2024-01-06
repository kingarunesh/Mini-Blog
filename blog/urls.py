from django.urls import path

from blog.views import blog, blog_details


urlpatterns = [
    path("blog/", view=blog, name="blog"),
    path("blog/<int:blog_id>/", view=blog_details, name="blog_details")
]
