from django.urls import path, include
from rest_framework.routers import DefaultRouter
from scrapPlasti import views

router = DefaultRouter()
router.register(r'tabla-scrap', views.TablaScrapViewSet, basename='scraptable')

urlpatterns = [
    path('tables/', include(router.urls)),
]
