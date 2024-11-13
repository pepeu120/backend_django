from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'livros', views.LivroViewSet)
router.register(r'autores', views.AutorViewSet)
router.register(r'categorias', views.CategoriaViewSet)

urlpatterns = router.urls