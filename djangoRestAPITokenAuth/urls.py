"""djangoRestAPITokenAuth URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from CRUD import views
from rest_framework_simplejwt import views as jwt_views
from main import views as main_views

router = routers.DefaultRouter()  # add this
router.register(r'posts', views.PostView, 'Crud')  # add this

urlpatterns = [
  path('admin/', admin.site.urls),
  path('hello/', main_views.HelloView.as_view(), name='hello'),
  path('api/', include(router.urls)),
  path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
  path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
]

"""
from main import views as main_views
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('CRUD.urls')),
    path('hello/', main_views.HelloView.as_view(), name='hello'),
] """
