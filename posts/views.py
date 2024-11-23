from django.shortcuts import render
#De la facilidad de las vistas genericas de django importo un ListView
from django.views.generic import ListView
#Importando el modelo de datos
from .models import Publication
# Create your views here.
#Vistas basadas en clases

class PostListView(ListView):
    #El modelo que quiero mostrar
    model = Publication
    template_name = "post_list.html"
