from django.urls import include, path
from rest_framework import routers
from .views import PostView, CategoryView, comment_list, like

router = routers.DefaultRouter()

router.register('blog', PostView)
router.register('categories', CategoryView)


urlpatterns = [
    path("", include(router.urls)),
    path("likes/<int:pk>/", like, name="like"),
    path("comments/<int:pk>/", comment_list, name="comment_list"),
]