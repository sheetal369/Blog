from rest_framework.routers import DefaultRouter
from .views import  PostViewSet

router = DefaultRouter()
router.register(r'users', PostViewSet, basename='user') # The 'users' string represents the base URL path for the posts resource
urlpatterns = router.urls