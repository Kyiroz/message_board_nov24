from django.urls import path
# Para importar la clase de la vista
from .views import PostListView

urlpatterns = [
    # El path es el que se va a mostrar en la url
    # El nombre es el que se va a mostrar en el template
    # El view es la vista que se va a utilizar
    path("", PostListView.as_view(), name="post_list"),
]