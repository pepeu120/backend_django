from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register("livros", views.LivroViewSet)
router.register("autores", views.AutorViewSet)
router.register("categorias", views.CategoriaViewSet)
router.register("colecoes", views.ColecaoViewSet)

urlpatterns = router.urls
