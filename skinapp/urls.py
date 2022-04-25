from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from skinapp.views import *

app_name = "ebdjango"

urlpatterns = [
    path('register/', registration_view, name="register"),
    path('login/', TokenObtainPairView.as_view(), name="login"),
    path('predict/', UploadView.as_view(), name="prediction"),

]
