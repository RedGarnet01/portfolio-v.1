from django.urls import path
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', TemplateView.as_view(template_name='portfolio/about.html'), name='about'),

]
