from django.test import TestCase
from factures.models import Facture, Client, Categorie

class FactureModelTest(TestCase):
    def setUp(self):
        self.client = Client.objects.create(nom="Alexandre RASPAUD", email="alexandre.raspaud@snowlab.fr")
        self.categorie = Categorie.objects.create(nom="Python")
        self.facture = Facture.objects.create(
            titre="Développement django",
            montant=2.00,
            client=self.client,
            categorie=self.categorie
        )

    def test_str_method(self):
        self.assertEqual(str(self.facture), "Développement django - 2.00 €")

    def test_default_statut_non_paye(self):
        self.assertFalse(self.facture.paye)

    def test_date_creation_auto(self):
        self.assertIsNotNone(self.facture.date_creation)
