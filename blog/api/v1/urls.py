from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter


app_name = "api.v1"

router = DefaultRouter()
router.register("post", views.PostModelViewSet, basename="post")
router.register("Category", views.CategoryModelViewSet, basename="category")
urlpatterns = router.urls




# urlpatterns = [

#     path("post/", views.PostList.as_view(), name="post_list"),
#     path("post/<int:pk>/", views.PostDetail.as_view(), name="post_detail"),
# ]