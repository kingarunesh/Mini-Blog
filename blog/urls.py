from django.urls import path

from blog.views import blog, blog_details, add_blog


urlpatterns = [
    path("blog/", view=blog, name="blog"),
    path("blog/<int:blog_id>/", view=blog_details, name="blog_details"),
    path("add-blog/", view=add_blog, name="add_blog")
]
