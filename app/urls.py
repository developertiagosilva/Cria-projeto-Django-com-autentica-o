from django.urls import path

from . import views


from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', views.index, name="index"),
    # path("logout/",LogoutView.as_view(), name="sair",),
    path("sair/", views.sair, name="sair"),
    path("painel/", views.painel, name="painel"),

]
