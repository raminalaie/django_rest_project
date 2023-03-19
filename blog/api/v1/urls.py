from django.urls import path, include
from . import views



app_name = "api.v1"


urlpatterns = [

    path("post/", views.api_post_list_view, name="post_list"),
    path("post/<int:id>/", views.api_post_detail_view, name="post_detail"),
]