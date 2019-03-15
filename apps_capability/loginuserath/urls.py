from django.conf.urls import url, include
from knox import views as knox_views
from .views import Login_Api

urlpatterns = [
    url(r'^api-auth/',include('knox.urls')),
    url(r'^api-auth/userlogin',Login_Api.as_view()),
]