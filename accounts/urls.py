from django.urls import include,path
from django.contrib import admin
from rest_framework import routers
from .views import SignupViewSet, LoginView, ImageViewSet



router = routers.DefaultRouter()
router.register('signup', SignupViewSet),
router.register('image', ImageViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('login/',LoginView.as_view(),name='login'),

]
