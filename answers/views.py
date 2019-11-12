from django.shortcuts import render, get_object_or_404, redirect
from .forms import CommentForm
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.views.generic.base import RedirectView
from questions.models import Savolho
from .models import Comment
# from django.contrib.contenttypes.models import ContentType
from django.contrib import messages
from django.views.generic import DetailView

