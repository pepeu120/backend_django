from rest_framework.test import APITestCase, APIClient
from django.urls import reverse
from rest_framework import status
from core.models import Autor, Categoria, Livro, Colecao
from django.contrib.auth.models import User


class CategoriaViewSetTest(APITestCase):

    def setUp(self):
        self.client = APIClient()
        self.categoria = Categoria.objects.create(nome="Ficção")

    def test_categoria_list(self):
        url = reverse("categoria-list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["count"], 1)

    def test_categoria_create(self):
        url = reverse("categoria-list")
        data = {"nome": "Aventura"}
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Categoria.objects.count(), 2)
        self.assertEqual(Categoria.objects.get(pk=response.data["pk"]).nome, "Aventura")

    def test_categoria_retrieve(self):
        url = reverse("categoria-detail", args=[self.categoria.pk])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["nome"], self.categoria.nome)

    def test_categoria_update(self):
        url = reverse("categoria-detail", args=[self.categoria.pk])
        data = {"nome": "Mistério"}
        response = self.client.put(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.categoria.refresh_from_db()
        self.assertEqual(self.categoria.nome, "Mistério")

    def test_categoria_delete(self):
        url = reverse("categoria-detail", args=[self.categoria.pk])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Categoria.objects.count(), 0)


class AutorViewSetTest(APITestCase):

    def setUp(self):
        self.client = APIClient()
        self.autor = Autor.objects.create(nome="J.K. Rowling")

    def test_autor_list(self):
        url = reverse("autor-list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["count"], 1)

    def test_autor_create(self):
        url = reverse("autor-list")
        data = {"nome": "George Orwell"}
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Autor.objects.count(), 2)
        self.assertEqual(
            Autor.objects.get(pk=response.data["pk"]).nome, "George Orwell"
        )

    def test_autor_retrieve(self):
        url = reverse("autor-detail", args=[self.autor.pk])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["nome"], self.autor.nome)

    def test_autor_update(self):
        url = reverse("autor-detail", args=[self.autor.pk])
        data = {"nome": "J.R.R. Tolkien"}
        response = self.client.put(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.autor.refresh_from_db()
        self.assertEqual(self.autor.nome, "J.R.R. Tolkien")

    def test_autor_delete(self):
        url = reverse("autor-detail", args=[self.autor.pk])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Autor.objects.count(), 0)


class LivroViewSetTest(APITestCase):

    def setUp(self):
        self.client = APIClient()
        self.categoria = Categoria.objects.create(nome="Fantasia")
        self.autor = Autor.objects.create(nome="J.K. Rowling")
        self.livro = Livro.objects.create(
            titulo="Harry Potter e a Pedra Filosofal",
            autor=self.autor,
            categoria=self.categoria,
            publicado_em="1997-06-26",
        )

    def test_livro_list(self):
        url = reverse("livro-list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["count"], 1)

    def test_livro_create(self):
        url = reverse("livro-list")
        data = {
            "titulo": "Harry Potter e a Câmara Secreta",
            "autor": self.autor.nome,
            "categoria": self.categoria.nome,
            "publicado_em": "1998-07-02",
        }
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Livro.objects.count(), 2)
        livro = Livro.objects.get(pk=response.data["pk"])
        self.assertEqual(livro.titulo, "Harry Potter e a Câmara Secreta")

    def test_livro_retrieve(self):
        url = reverse("livro-detail", args=[self.livro.pk])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["titulo"], self.livro.titulo)

    def test_livro_update(self):
        url = reverse("livro-detail", args=[self.livro.pk])
        data = {
            "titulo": "Harry Potter e o Prisioneiro de Azkaban",
            "autor": self.autor.nome,
            "categoria": self.categoria.nome,
            "publicado_em": "1999-07-08",
        }
        response = self.client.put(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.livro.refresh_from_db()
        self.assertEqual(self.livro.titulo, "Harry Potter e o Prisioneiro de Azkaban")

    def test_livro_delete(self):
        url = reverse("livro-detail", args=[self.livro.pk])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Livro.objects.count(), 0)


class ColecaoViewSetTest(APITestCase):

    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username="testuser", password="testpass")
        self.user2 = User.objects.create_user(
            username="otheruser", password="otherpass"
        )
        self.categoria = Categoria.objects.create(nome="Fantasia")
        self.autor = Autor.objects.create(nome="J.K. Rowling")
        self.livro = Livro.objects.create(
            titulo="Harry Potter e a Pedra Filosofal",
            autor=self.autor,
            categoria=self.categoria,
            publicado_em="1997-06-26",
        )
        self.colecao = Colecao.objects.create(
            nome="Minha Coleção",
            descricao="Descrição da coleção",
            colecionador=self.user,
        )
        self.colecao.livros.add(self.livro)

    def test_colecao_list(self):
        url = reverse("colecao-list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["count"], 1)

    def test_colecao_create_unauthenticated(self):
        url = reverse("colecao-list")
        data = {
            "nome": "Nova Coleção",
            "descricao": "Descrição",
            "livros": [self.livro.pk],
        }
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_colecao_create_authenticated(self):
        self.client.force_authenticate(user=self.user)
        url = reverse("colecao-list")
        data = {
            "nome": "Nova Coleção",
            "descricao": "Descrição",
            "livros": [self.livro.pk],
        }
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Colecao.objects.count(), 2)
        colecao = Colecao.objects.get(pk=response.data["id"])
        self.assertEqual(colecao.nome, "Nova Coleção")
        self.assertEqual(colecao.colecionador, self.user)

    def test_colecao_retrieve(self):
        url = reverse("colecao-detail", args=[self.colecao.pk])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["nome"], self.colecao.nome)

    def test_colecao_update_owner(self):
        self.client.force_authenticate(user=self.user)
        url = reverse("colecao-detail", args=[self.colecao.pk])
        data = {"nome": "Coleção Atualizada", "descricao": "Nova descrição"}
        response = self.client.patch(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.colecao.refresh_from_db()
        self.assertEqual(self.colecao.nome, "Coleção Atualizada")
        self.assertEqual(self.colecao.descricao, "Nova descrição")

    def test_colecao_update_non_owner(self):
        self.client.force_authenticate(user=self.user2)
        url = reverse("colecao-detail", args=[self.colecao.pk])
        data = {"nome": "Tentativa de Atualização"}
        response = self.client.patch(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_colecao_delete_owner(self):
        self.client.force_authenticate(user=self.user)
        url = reverse("colecao-detail", args=[self.colecao.pk])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Colecao.objects.count(), 0)

    def test_colecao_delete_non_owner(self):
        self.client.force_authenticate(user=self.user2)
        url = reverse("colecao-detail", args=[self.colecao.pk])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(Colecao.objects.count(), 1)
