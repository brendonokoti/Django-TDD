from django.shortcuts import render
from animais.models import Animal

def index(request):
    context = {"caracteristicas": None}
    if "buscar" in request.GET:
        animais = Animal.objects.all()
        animal_pesquisado = request.get["buscar"]
        caracteristicas = animais.filter(nome_popular__icontais=animal_pesquisado)
        context = {"caracteristicas": caracteristicas}
    return render(request, "index.html", context)