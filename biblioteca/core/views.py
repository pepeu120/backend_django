from rest_framework import viewsets, generics, permissions
from .models import Autor, Categoria, Colecao, Livro
from .serializers import AutorSerializer, CategoriaSerializer, ColecaoSerializer, LivroSerializer

class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer


class AutorViewSet(viewsets.ModelViewSet):
    queryset = Autor.objects.all()
    serializer_class = AutorSerializer


class LivroViewSet(viewsets.ModelViewSet):
    queryset = Livro.objects.all()
    serializer_class = LivroSerializer


class ColecaoListCreate(generics.ListCreateAPIView):
    queryset = Colecao.objects.all()
    serializer_class = ColecaoSerializer
    permission_classes = [permissions.IsAuthenticated]


class ColecaoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Colecao.objects.all()
    serializer_class = ColecaoSerializer
    permission_classes = [permissions.IsAuthenticated, IsColecionador]