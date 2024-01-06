from django.urls import path

from blog.views import blog, blog_details, add_blog, delete_blog


urlpatterns = [
    path("blog/", view=blog, name="blog"),
    path("blog/<int:blog_id>/", view=blog_details, name="blog_details"),
    path("add-blog/", view=add_blog, name="add_blog"),
    path("delete-blog/<int:blog_id>/", view=delete_blog, name="delete_blog")
]
