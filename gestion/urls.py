from django.urls import path, include
from gestion import views
from gestion.views import (
    TemaDetailView,
    TemaCreateView,
    TemaUpdateView,
    TemaDeleteView,
    TemasListView,
)

urlpatterns = [
    path("", views.home, name="home"),
    path("signup/", views.signup, name="signup"),
    path("login/", views.signin, name="login"),
    path("logout/", views.signout, name="logout"),
    path("temas/", TemasListView.as_view(), name="temas_list"),
    path("temas/<int:pk>", TemaDetailView.as_view(), name="tema_detail"),
    path("temas/create", TemaCreateView.as_view(), name="create_tema"),
    path("temas/<int:pk>/update", TemaUpdateView.as_view(), name="update_tema"),
    path("temas/<int:pk>/delete", TemaDeleteView.as_view(), name="delete_tema"),
]
