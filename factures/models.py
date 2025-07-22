from django.db import models

class Categorie(models.Model):
    nom = models.CharField(max_length=100)

    def __str__(self):
        return self.nom

class Client(models.Model):
    nom = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return self.nom

class Facture(models.Model):
    titre = models.CharField(max_length=200)
    montant_ht = models.DecimalField(max_digits=10, decimal_places=2)
    tva = models.DecimalField(max_digits=4, decimal_places=2, default=20.0)
    date_creation = models.DateField(auto_now_add=True)
    paye = models.BooleanField(default=False)
    categorie = models.ForeignKey(Categorie, null=True, blank=True, on_delete=models.SET_NULL)
    client = models.ForeignKey(Client, null=False, blank=False, on_delete=models.CASCADE)

    @property
    def montant_ttc(self):
        return round(self.montant_ht * (1 + self.tva / 100), 2)

    def __str__(self):
        return f"{self.titre} - {self.montant_ttc:.2f} €"
