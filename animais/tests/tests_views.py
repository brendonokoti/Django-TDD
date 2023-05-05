from django.test import TestCase, RequestFactory
from django.db.models.query import QuerySet
from animais.models import Animal

class IndexViewTestCase(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.animal = Animal.objects.create(
            nome_cientifico="Harpia harpyja",
            nome_popular="Gavião-real",
            predador=True,
            venenoso=False,
            domestico=False
        )
    
    def test_index_view_retorna_caracteristicas_do_animal(self):
        """Teste: verifica se a index retorna as características do animal."""
        response = self.client.get("/",
            {"buscar": "calopsita"}                  
        )
        caracteristica_animal_pesquisado = response.context["caracteristica"]
        self.assertIs(type(response.context["caracteristicas"]), QuerySet)
        self.assertEqual(caracteristica_animal_pesquisado[0], "calopsita")
