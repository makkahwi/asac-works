from django.shortcuts import render
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    TemplateView,
    UpdateView,
)

from .models import Snack


class SnackListView(ListView):
    template_name = "snack_list.html"
    model = Snack


class SnacksDetailView(DetailView):
    template_name = "snack_detail.html"
    model = Snack


class SnackCreateView(CreateView):
    template_name = "snack_create.html"
    model = Snack
    fields = [
        "title",
        "purchaser",
        "desc",
        "calories",
        "vegan",
        "gloten_free",
        "sugar_free",
        "lactose_free",
    ]


class SnackUpdateView(UpdateView):
    template_name = "snack_update.html"
    model = Snack
    fields = [
        "title",
        "purchaser",
        "desc",
        "calories",
        "vegan",
        "gloten_free",
        "sugar_free",
        "lactose_free",
    ]


class SnackDeleteView(DeleteView):
    template_name = "snack_delete.html"
    model = Snack
    success_url = "/"


class AboutView(TemplateView):
    template_name = "about.html"
    model = Snack
