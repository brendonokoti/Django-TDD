from django.test import TestCase, RequestFactory
from animais.models import Animal

class AnimalModelTestCase(TestCase):

    def setUp(self):
        self.animal = Animal.objects.create(
            nome_cientifico = "Panthera leo",
            nome_popular = "Leão",
            predador = True,
            venenoso = False,
            domestico = False
        )

    def test_animal_cadastrado_com_caracteristicas(self):
        """Teste: verifica se o animal está cadastrado com suas características."""
        self.assertEqual(self.animal.nome_popular, "Leão")