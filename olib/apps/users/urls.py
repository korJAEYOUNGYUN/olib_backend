from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from olib.apps.users import views

urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('user/', views.UserView.as_view(), name='user'),
]
