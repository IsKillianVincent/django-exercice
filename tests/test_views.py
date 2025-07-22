from django.test import TestCase
from django.urls import reverse
from factures.models import Facture, Client, Categorie

class FactureViewsTest(TestCase):
    def setUp(self):
        self.client_obj = Client.objects.create(nom="Alexandre RASPAUD", email="alexandre.raspaud@snowlab.fr")
        self.categorie = Categorie.objects.create(nom="Python")
        self.facture = Facture.objects.create(
            titre="Développement django",
            montant=2.00,
            client=self.client_obj,
            categorie=self.categorie
        )

    def test_liste_factures_status_code(self):
        response = self.client.get(reverse('liste_factures'))
        self.assertEqual(response.status_code, 200)

    def test_liste_factures_affiche_titre(self):
        response = self.client.get(reverse('liste_factures'))
        self.assertContains(response, "Développement django")

    def test_liste_factures_filtrage_client(self):
        response = self.client.get(reverse('liste_factures'), {'client': self.client_obj.id})
        self.assertEqual(len(response.context['factures']), 1)

    def test_detail_facture_status(self):
        response = self.client.get(reverse('detail_facture', args=[self.facture.id]))
        self.assertEqual(response.status_code, 200)

    def test_detail_facture_affiche_montant(self):
        response = self.client.get(reverse('detail_facture', args=[self.facture.id]))
        self.assertContains(response, "2.00")

    def test_detail_facture_not_found(self):
        response = self.client.get(reverse('detail_facture', args=[999]))
        self.assertEqual(response.status_code, 404)

    def test_creer_facture_status(self):
        response = self.client.get(reverse('creer_facture'))
        self.assertEqual(response.status_code, 200)

    def test_creer_facture_post_valide(self):
        response = self.client.post(reverse('creer_facture'), {
            'titre': 'Développement django v2',
            'montant': 4,
            'client': self.client_obj.id,
            'categorie': self.categorie.id,
            'paye': False
        })
        self.assertEqual(Facture.objects.count(), 2)

    def test_creer_facture_redirection_apres_creation(self):
        response = self.client.post(reverse('creer_facture'), {
            'titre': 'Facture mobile',
            'montant': 60,
            'client': self.client_obj.id,
            'categorie': self.categorie.id,
            'paye': True
        })
        self.assertRedirects(response, reverse('liste_factures'))
