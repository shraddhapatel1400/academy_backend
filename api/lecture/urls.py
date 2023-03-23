from rest_framework import routers
from django.urls import path,include

from . import views

router = routers.DefaultRouter()
router.register(r'', views.LectureViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('sendmail/', views.send_mail)
]