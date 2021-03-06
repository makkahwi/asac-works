from django.shortcuts import render
from django.views.generic import DetailView, ListView, TemplateView

from .models import Snack


class SnackListView(ListView):
    template_name = "snack_list.html"
    model = Snack


class SnacksDetailView(DetailView):
    template_name = "snack_detail.html"
    model = Snack


class AboutView(TemplateView):
    template_name = "about.html"
    model = Snack
