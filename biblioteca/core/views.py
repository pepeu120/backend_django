from rest_framework import viewsets, generics, views
from .models import Autor, Categoria, Livro, Colecao, Colecionador
from .serializers import AutorSerializer, CategoriaSerializer, ColecaoSerializer, LivroSerializer, \
    ColecionadorSerializer


class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

class AutorViewSet(viewsets.ModelViewSet):
    queryset = Autor.objects.all()
    serializer_class = AutorSerializer

class LivroViewSet(viewsets.ModelViewSet):
    queryset = Livro.objects.all()
    serializer_class = LivroSerializer


class ColecionadorViewSet(viewsets.ModelViewSet):
    queryset = Colecionador.objects.all()
    serializer_class = ColecionadorSerializer


class ColecaoViewSet(viewsets.ModelViewSet):
    queryset = Colecao.objects.all()
    serializer_class = ColecaoSerializer
