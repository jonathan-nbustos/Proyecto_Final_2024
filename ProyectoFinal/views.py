from django.http import HttpResponse
from django.template import Template, Context 
from django.template import loader
import datetime

def saludo(request):
    return HttpResponse("Hola Django - Coder")


def dia_de_hoy(request):
    dia = datetime.datetime.now()
    documentoDeTexto = f"Hoy es día <br> {dia}"
    return HttpResponse(documentoDeTexto)

def miNombreEs(self, nombre):
    documentoDeTexto = f"Mi nombre <br><br>{nombre}"
    return HttpResponse(documentoDeTexto)

def probando_template(request):

    nombre = "Luis"
    apellido = "Perez"
    lista_de_notas = {1,2,3,5,8,3,7}

    diccionario = {'nombre': nombre,'apellido': apellido, 'hoy':datetime.datetime.now(),'notas': lista_de_notas}
    plantilla = loader.get_template("template1.html")
    documento = plantilla.render(diccionario)

    return HttpResponse(documento)
