from rest_framework import serializers, relations

from .models import Categoria, Autor, Livro, Colecao, Colecionador

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


class ColecionadorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Colecionador
        exclude = ('last_login',)


class ColecaoSerializer(serializers.HyperlinkedModelSerializer):
    livros = serializers.SerializerMethodField()
    colecionador = serializers.SlugRelatedField(queryset=Colecionador.objects.all(), slug_field='username')

    class Meta:
        model = Colecao
        fields = ('url', 'pk', 'colecionador', 'nome', 'descricao', 'livros')

    def get_livros(self, obj):
        return [livro.titulo for livro in obj.livros.all()]
