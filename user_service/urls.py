# =================================================================================================
#                                  All Rights Reserved.
# =================================================================================================
# File description:
#
#       Ref: https://www.django-rest-framework.org/api-guide/routers/
#
# =================================================================================================
#    Date      Name                    Description of Change
# 15-Feb-2023  Wayne Shih              Initial create
# $HISTORY$
# =================================================================================================

"""user_service URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import include, path
from rest_framework import routers

from accounts.api.views import UserViewSet


router = routers.DefaultRouter()
router.register(r'api/users', UserViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
