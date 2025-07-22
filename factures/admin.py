from django.contrib import admin
from .models import Facture, Client, Categorie

@admin.register(Facture)
class FactureAdmin(admin.ModelAdmin):
    list_display = ('id', 'titre', 'client', 'montant_ht', 'tva', 'montant_ttc', 'categorie', 'paye', 'date_creation')
    list_filter = ('client', 'paye')
    search_fields = ('titre', 'client__nom')
    actions = ['marquer_comme_paye', 'marquer_comme_impaye']
    # les def doivent avoir même nom que la variable attention

    @admin.action(description="Marquer comme payée")
    def marquer_comme_paye(self, request, queryset):
        updated = queryset.update(paye=True)
        self.message_user(request, f"{updated} facture(s) marquée(s) comme payée(s).")

    @admin.action(description="Marquer comme impayée")
    def marquer_comme_impaye(self, request, queryset):
        queryset.update(paye=False)
        self.message_user(request, "Factures marquées comme impayées.")

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('nom', 'email')
    search_fields = ('nom',)

@admin.register(Categorie)
class CategorieAdmin(admin.ModelAdmin):
    list_display = ('nom',)
    search_fields = ('nom',)