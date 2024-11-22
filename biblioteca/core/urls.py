from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'livros', views.LivroViewSet)
router.register(r'autores', views.AutorViewSet)
router.register(r'categorias', views.CategoriaViewSet)
router.register('colecoes', views.ColecaoViewSet)
router.register('colecionadores', views.ColecionadorViewSet)

urlpatterns = router.urls