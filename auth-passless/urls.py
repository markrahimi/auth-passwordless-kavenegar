from django.urls import include, path

app_name = "auth-pass-less"

from rest_framework_simplejwt.views import (
    TokenRefreshView,
)
from drfpasswordless.views import (
     ObtainMobileCallbackToken,
     ObtainAuthTokenFromCallbackToken,
)

urlpatterns = [
    path('auth/login/', ObtainMobileCallbackToken.as_view(), name='auth_mobile'),
    path('auth/verify/', ObtainAuthTokenFromCallbackToken.as_view(), name='auth_token'),
    path('auth/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]