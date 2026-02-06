from django.urls import path

from . import views
from rest_framework.routers import SimpleRouter



router = SimpleRouter()
router.register('posts', views.PostViewSet)

urlpatterns = router.urls

# urlpatterns = [
#     path('', views.PostViewSet.as_view({'get': 'list'}), name='post-list'),
#     path('post/<int:pk>/', views.PostViewSet.as_view({'get': 'list'}), name='post-detail'),
#     path('post/new/', views.PostViewSet.as_view({'get': 'list'}), name='post-new'),
#     path('post/<int:pk>/edit/', views.PostViewSet.as_view({'get': 'list'}), name='post-edit'),
# ]