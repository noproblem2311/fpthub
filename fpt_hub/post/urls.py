from .views import PostViewSet, TopicViewSet

from rest_framework.routers import DefaultRouter



router = DefaultRouter()
router.register('Posts', PostViewSet, basename='posts')
router.register('Topics', TopicViewSet, basename='topics')
urlpatterns = [
    
  
]
urlpatterns += router.urls