from django.shortcuts import render, get_object_or_404, redirect
from .models import Facture, Categorie, Client
from .forms import FactureForm

def liste_factures(request):
    client_id = request.GET.get('client')
    query = request.GET.get('q')
    factures = Facture.objects.all()
    if client_id:
        factures = factures.filter(client__id=client_id)
    if query:
        factures = factures.filter(titre__icontains=query)
    clients = Client.objects.all()

    return render(request, 'factures/liste.html', {
        'factures': factures,
        'clients': clients,
    })

def detail_facture(request, pk):
    facture = get_object_or_404(Facture, pk=pk)
    return render(request, 'factures/detail.html', {'facture': facture})

def creer_facture(request):
    if request.method == 'POST':
        form = FactureForm(request.POST)
        if form.is_valid():
            facture = form.save(commit=False)
            if not facture.categorie:
                autres, _ = Categorie.objects.get_or_create(nom="Autres")
                facture.categorie = autres
            facture.save()
            return redirect('liste_factures')
    else:
        form = FactureForm()
    return render(request, 'factures/formulaire.html', {'form': form})

def modifier_facture(request, pk):
    facture = get_object_or_404(Facture, pk=pk)
    if request.method == 'POST':
        form = FactureForm(request.POST, instance=facture)
        if form.is_valid():
            facture = form.save(commit=False)
            if not facture.categorie:
                autres, _ = Categorie.objects.get_or_create(nom="Autres")
                facture.categorie = autres
            facture.save()
            return redirect('liste_factures')
    else:
        form = FactureForm(instance=facture)
    return render(request, 'factures/formulaire.html', {'form': form})

def supprimer_facture(request, pk):
    facture = get_object_or_404(Facture, pk=pk)
    if request.method == 'POST':
        facture.delete()
        return redirect('liste_factures')
    return render(request, 'factures/confirm_suppression.html', {'facture': facture})
