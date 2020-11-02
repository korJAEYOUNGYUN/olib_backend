from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from olib.apps.users import views

urlpatterns = [
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/user/', views.UserView.as_view(), name='user'),
]
