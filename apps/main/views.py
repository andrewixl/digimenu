from django.shortcuts import render
from .models import Menu
from django.http import FileResponse

# Create your views here.
def index(request):
    return render( request, 'main/Dennys-Menu.html')

def menu(request, slug):
    menu = Menu.objects.get(slug=slug)
    print (menu.menuPDF)
    return FileResponse(open("media/" + str(menu.menuPDF), 'rb'), content_type='application/pdf')
