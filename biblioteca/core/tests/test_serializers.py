from django.test import TestCase
from core.models import Autor, Categoria, Livro, Colecao
from core.serializers import (
    AutorSerializer,
    CategoriaSerializer,
    LivroSerializer,
    ColecaoSerializer,
)
from django.contrib.auth.models import User
from rest_framework.exceptions import ValidationError


class CategoriaSerializerTest(TestCase):

    def test_categoria_serializer(self):
        data = {"nome": "Ficção"}
        serializer = CategoriaSerializer(data=data)
        self.assertTrue(serializer.is_valid())
        categoria = serializer.save()
        self.assertEqual(categoria.nome, "Ficção")


class AutorSerializerTest(TestCase):

    def test_autor_serializer(self):
        data = {"nome": "J.K. Rowling"}
        serializer = AutorSerializer(data=data)
        self.assertTrue(serializer.is_valid())
        autor = serializer.save()
        self.assertEqual(autor.nome, "J.K. Rowling")


class LivroSerializerTest(TestCase):

    def test_livro_serializer(self):
        categoria = Categoria.objects.create(nome="Fantasia")
        autor = Autor.objects.create(nome="J.K. Rowling")
        data = {
            "titulo": "Harry Potter e a Pedra Filosofal",
            "autor": autor.nome,
            "categoria": categoria.nome,
            "publicado_em": "1997-06-26",
        }
        serializer = LivroSerializer(data=data)
        self.assertTrue(serializer.is_valid(), serializer.errors)
        livro = serializer.save()
        self.assertEqual(livro.titulo, "Harry Potter e a Pedra Filosofal")
        self.assertEqual(livro.autor, autor)
        self.assertEqual(livro.categoria, categoria)
        self.assertEqual(str(livro.publicado_em), "1997-06-26")


class ColecaoSerializerTest(TestCase):

    def test_colecao_serializer(self):
        user = User.objects.create_user(username="testuser", password="testpass")
        livro1 = Livro.objects.create(
            titulo="Livro 1",
            autor=Autor.objects.create(nome="Autor 1"),
            categoria=Categoria.objects.create(nome="Categoria 1"),
            publicado_em="2000-01-01",
        )
        livro2 = Livro.objects.create(
            titulo="Livro 2",
            autor=Autor.objects.create(nome="Autor 2"),
            categoria=Categoria.objects.create(nome="Categoria 2"),
            publicado_em="2001-01-01",
        )
        data = {
            "nome": "Minha Coleção",
            "descricao": "Descrição da coleção",
            "livros": [livro1.pk, livro2.pk],
            "colecionador": user.pk,
        }
        serializer = ColecaoSerializer(data=data)
        self.assertTrue(serializer.is_valid(), serializer.errors)
        colecao = serializer.save()
        self.assertEqual(colecao.nome, "Minha Coleção")
        self.assertEqual(colecao.descricao, "Descrição da coleção")
        self.assertEqual(colecao.colecionador, user)
        self.assertQuerysetEqual(
            colecao.livros.all(), [livro1.pk, livro2.pk], transform=lambda x: x.pk
        )
