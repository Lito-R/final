from django.urls import path
from . import views

urlpatterns = [
        path("", views.home, name="home"),
        path("agregartarea/",views.agregartarea, name="agregartarea"),
        path("eliminar/<int:tarea_id>/", views.eliminartarea, name= "eliminartarea"),
        path("editar/<int:tarea_id>/", views.editartarea, name="editartarea"),
]