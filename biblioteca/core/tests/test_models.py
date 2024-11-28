from django.test import TestCase
from django.contrib.auth.models import User
from core.models import Autor, Categoria, Livro, Colecao
from django.utils import timezone


class CategoriaModelTest(TestCase):

    def test_categoria_creation(self):
        categoria = Categoria.objects.create(nome="Ficção Científica")
        self.assertEqual(categoria.nome, "Ficção Científica")
        self.assertEqual(str(categoria), "Ficção Científica")


class AutorModelTest(TestCase):

    def test_autor_creation(self):
        autor = Autor.objects.create(nome="Isaac Asimov")
        self.assertEqual(autor.nome, "Isaac Asimov")
        self.assertEqual(str(autor), "Isaac Asimov")


class LivroModelTest(TestCase):

    def test_livro_creation(self):
        autor = Autor.objects.create(nome="Isaac Asimov")
        categoria = Categoria.objects.create(nome="Ficção Científica")
        publicado_em = date(1951, 1, 1)
        livro = Livro.objects.create(
            titulo="Fundação",
            autor=autor,
            categoria=categoria,
            publicado_em=publicado_em,
        )
        self.assertEqual(livro.titulo, "Fundação")
        self.assertEqual(livro.autor, autor)
        self.assertEqual(livro.categoria, categoria)
        self.assertEqual(livro.publicado_em, publicado_em)
        self.assertEqual(str(livro), "Fundação")


class ColecaoModelTest(TestCase):

    def test_colecao_creation(self):
        user = User.objects.create_user(username="testuser", password="testpass")
        colecao = Colecao.objects.create(
            nome="Minha Coleção", descricao="Descrição da coleção", colecionador=user
        )
        self.assertEqual(colecao.nome, "Minha Coleção")
        self.assertEqual(colecao.descricao, "Descrição da coleção")
        self.assertEqual(colecao.colecionador, user)
        self.assertEqual(str(colecao), "Minha Coleção - testuser")
