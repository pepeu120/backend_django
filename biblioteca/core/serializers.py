from rest_framework import serializers
from .models import Categoria, Autor, Livro
#from .views import CategoriaViewSet, AutorViewSet, LivroViewSet

class CategoriaSerializer(serializers.HyperlinkedModelSerializer):
    livros = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='Livro Instance')

    class Meta:
        model = Categoria
        fields = ('url', 'pk', 'nome', 'livros')


class AutorSerializer(serializers.HyperlinkedModelSerializer):
    livros = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='livros')

    class Meta:
        model = Autor
        fields = ('url', 'pk', 'nome', 'livros')


class LivroSerializer(serializers.HyperlinkedModelSerializer):
    categoria = serializers.SlugRelatedField(queryset=Categoria.objects.all(), slug_field='nome')
    autor = serializers.SlugRelatedField(queryset=Autor.objects.all(), slug_field='nome')

    class Meta:
        model = Livro
        fields = ('url', 'pk', 'titulo', 'autor', 'categoria', 'publicado_em')
