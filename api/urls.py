from django.urls import include, path
from rest_framework import routers
from api.viewsets import UserViewSet, BlogApiView, PostAPIView

router = routers.DefaultRouter()
router.register(r'users', UserViewSet, basename='user')


urlpatterns = [
    path('', include((router.urls, 'api'))),
    path('auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('blog/', BlogApiView.as_view()),
    path('anton/', PostAPIView.as_view()),
]