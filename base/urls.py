from django.urls import path, include
from rest_framework.documentation import include_docs_urls
from rest_framework import routers
from base import views

router = routers.DefaultRouter()
router.register(r"productos", views.ProductView, basename= 'producto')
router.register(r"proveedores", views.ProveedorView, basename= 'proveedor')
router.register(r"categorias", views.CategoriaView, basename= 'categorias')


urlpatterns = [
    path("api/v1/", include(router.urls)),
    path("docs/",include_docs_urls(title="stock API"))
]