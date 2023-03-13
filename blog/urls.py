from django.urls import path, include
from . import views

from django.views.generic.base import RedirectView
app_name = "blog"


urlpatterns = [
    path("cbv_index/", views.IndexView.as_view(), name="cbv_index"),
    path("got_to_index/",RedirectView.as_view(pattern_name="blog:cbv_index"), name="redirectView"),
    path("post/", views.PostList.as_view(), name="post_list"),
    path("post/<int:pk>/",views.PostDetailView.as_view(), name="post_detail"),
    path("post_create/", views.PostCreateView.as_view(), name="post_create"),
    path("post/<int:pk>/edit/", views.PostEditView.as_view(), name="post_edit"),
    path("post/<int:pk>/delete/", views.PstDeleteView.as_view(), name="post_delete"),

]