from django.urls import path
from . import views
from rest_framework_simplejwt.views import TokenRefreshView,TokenVerifyView



app_name = 'api_v1'


urlpatterns = [
    #create user
    path('register/',views.RegistrationApiView.as_view(),name='register'),

    #login Token
    path('token/login/',views.CustomObtainAuthToken.as_view(),name="token_login"),
    path('token/logout/',views.CustomDiscardAuthToken.as_view(),name="token_logout"),

    #login JWT
    path('jwt/create/',views.CustomTokenObtainPairView.as_view(),name='jwt_create'),
    path('jwt/refresh/',TokenRefreshView.as_view(),name='jwt_refresh'),
    path('jwt/verify/',TokenVerifyView.as_view(),name='jwt_verify'),

    #change password
    path('change_password/',views.ChangePasswordView.as_view(),name='change_password'),

    #profile
    path('profile/',views.ProfileView.as_view(),name='profile'),
]

