from django.test import TestCase
from carros.models import Carro

class TestCarrosModels(TestCase):
    @classmethod
    def setUpTestData(cls):
        Carro.objects.create(nome='Fiat Tester')

    def testCarroCampoNomeTamanho(self):
        carro = Carro.objects.get(id=1)
        tamanho = carro._meta.get_field('nome').max_length
        self.assertEquals(tamanho, 30)

    
    