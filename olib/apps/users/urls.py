from django.urls import path, include
from rest_framework import routers
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from olib.apps.users import views


router = routers.DefaultRouter()
router.register('borrowings', views.BorrowingViewSet, basename='borrowing')

urlpatterns = [
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/user/', views.UserView.as_view(), name='user'),
    path('api/', include(router.urls)),
]
