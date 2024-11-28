from rest_framework import viewsets, generics, permissions
from .models import Autor, Categoria, Colecao, Livro
from .custom_permissions import IsOwnerOrReadOnly
from .serializers import (
    AutorSerializer,
    CategoriaSerializer,
    ColecaoSerializer,
    LivroSerializer,
)


class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer


class AutorViewSet(viewsets.ModelViewSet):
    queryset = Autor.objects.all()
    serializer_class = AutorSerializer


class LivroViewSet(viewsets.ModelViewSet):
    queryset = Livro.objects.all()
    serializer_class = LivroSerializer


class ColecaoViewSet(viewsets.ModelViewSet):
    queryset = Colecao.objects.all()
    serializer_class = ColecaoSerializer
    permission_classes = [IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(colecionador=self.request.user)
