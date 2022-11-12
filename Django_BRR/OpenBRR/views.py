from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone

# Create your views here.

# Función que recibe la petición post_main y devuelve un HTML
def post_main(request):
    return render(request, 'OpenBRR/main.html', {})