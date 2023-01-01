from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect


from django.views.generic import (
    ListView,
    DetailView,
    FormView,
    CreateView,
    UpdateView,
    DeleteView,
)


from .models import Tema
from .forms import TemaForm


# Create your views here.


# Signin Signup Signout


def signup(request):
    if request.method == "GET":
        return render(request, "signup.html", {"form": UserCreationForm})
    else:

        if request.POST["password1"] == request.POST["password2"]:
            try:
                user = User.objects.create_user(
                    request.POST["username"], password=request.POST["password1"]
                )
                user.save()
                login(request, user)
                return redirect("login")
            except IntegrityError:
                return render(
                    request,
                    "signup.html",
                    {"form": UserCreationForm, "error": "Username already exists."},
                )

        return render(
            request,
            "signup.html",
            {"form": UserCreationForm, "error": "Passwords did not match."},
        )


def signin(request):
    if request.method == "GET":
        return render(request, "login.html", {"form": AuthenticationForm})
    else:
        user = authenticate(
            request,
            username=request.POST["username"],
            password=request.POST["password"],
        )
        if user is None:
            return render(
                request,
                "login.html",
                {
                    "form": AuthenticationForm,
                    "error": "Username or password is incorrect.",
                },
            )

        login(request, user)
        return redirect("home")


@login_required
def signout(request):
    logout(request)
    return redirect("home")


# Home


def home(request):
    return render(request, "home.html")


# crud Tema
# listar
class TemasListView(ListView):
    model = Tema
    context_object_name = "lista_temas"
    template_name = "temas_list.html"


# ver
class TemaDetailView(DetailView):
    model = Tema
    template_name = "tema_detail.html"


# crear
class TemaCreateView(CreateView):
    model = Tema
    fields = ["titulo", "descripcion", "fuente"]
    template_name = "tema_create.html"
    success_url = "/temas"


# actualizar
class TemaUpdateView(UpdateView):
    model = Tema
    fields = ["titulo", "descripcion", "fuente"]
    template_name = "tema_update.html"
    success_url = "/temas"

    def post(self, request, *args, **kwargs):
        if "cancel" in request.POST:
            url = "/temas"
            return HttpResponseRedirect(url)
        else:
            return super(TemaUpdateView, self).post(request, *args, **kwargs)


# eliminar
class TemaDeleteView(DeleteView):
    model = Tema
    template_name = "tema_delete.html"
    success_url = "/temas"

    def post(self, request, *args, **kwargs):
        if "cancel" in request.POST:
            url = "/temas"
            return HttpResponseRedirect(url)
        else:
            return super(TemaDeleteView, self).post(request, *args, **kwargs)


# crud Perfiles
# # listar
# class TemasListView(ListView):
#     model = Tema
#     context_object_name = "lista_temas"
#     template_name = "temas_list.html"


# # ver
# class TemaDetailView(DetailView):
#     model = Tema
#     template_name = "tema_detail.html"


# # crear
# class TemaCreateView(CreateView):
#     model = Tema
#     fields = ["titulo", "descripcion", "fuente"]
#     template_name = "tema_create.html"
#     success_url = "/temas"


# # actualizar
# class TemaUpdateView(UpdateView):
#     model = Tema
#     fields = ["titulo", "descripcion", "fuente"]
#     template_name = "tema_update.html"
#     success_url = "/temas"

#     def post(self, request, *args, **kwargs):
#         if "cancel" in request.POST:
#             url = "/temas"
#             return HttpResponseRedirect(url)
#         else:
#             return super(TemaUpdateView, self).post(request, *args, **kwargs)


# # eliminar
# class TemaDeleteView(DeleteView):
#     model = Tema
#     template_name = "tema_delete.html"
#     success_url = "/temas"

#     def post(self, request, *args, **kwargs):
#         if "cancel" in request.POST:
#             url = "/temas"
#             return HttpResponseRedirect(url)
#         else:
#             return super(TemaDeleteView, self).post(request, *args, **kwargs)


# # crud Tema tesis
# @login_required
# def Temas(request):
#     Temas = Tema.objects.all()
#     return render(request, "temas.html", {"Temas": Temas})


# class TemaListView(ListView):
#     model = Tema
#     template_name = "Temas.html"


# class TemaDetailView(DetailView):
#     model = Tema
#     template_name = "Tema_detail.html"


# class TemaCreateView(CreateView):
#     model = Tema
#     template_name = "create_Tema.html"


# @login_required
# def create_Tema(request):
#     if request.method == "GET":
#         return render(request, "create_Tema.html", {"form": TemaForm})
#     else:
#         try:
#             form = TemaForm(request.POST)
#             new_Tema = form.save(commit=False)
#             new_Tema.user = request.user
#             new_Tema.save()
#             return redirect("Temas")
#         except ValueError:
#             return render(
#                 request,
#                 "create_Tema.html",
#                 {"form": TemaForm, "error": "Error creating task."},
#             )


# @login_required
# def Tema_detail(request, Tema_id):
#     if request.method == "GET":
#         Tema = get_object_or_404(Tema, pk=Tema_id, user=request.user)
#         form = TemaForm(instance=Tema)
#         return render(
#             request,
#             "Tema_detail.html",
#             {
#                 "Tema": Tema,
#                 "form": form,
#             },
#         )
#     else:
#         try:
#             Tema = get_object_or_404(Tema, pk=Tema_id, user=request.user)
#             form = TemaForm(request.POST, instance=Tema)
#             form.save()
#             return redirect("Temas")
#         except ValueError:
#             return render(
#                 request,
#                 "task_detail.html",
#                 {"Tema": Tema, "form": form, "error": "Error updating task."},
#             )


# @login_required
# def delete_Tema(request, Tema_id):
#     Tema = get_object_or_404(Tema, pk=Tema_id, user=request.user)
#     if request.method == "POST":
#         Tema.delete()
#         return redirect("Temas")
