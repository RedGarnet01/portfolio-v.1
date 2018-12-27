from django.shortcuts import render

def index(request):
    template_name = 'portfolio/header.html'
    return render(request, template_name)
