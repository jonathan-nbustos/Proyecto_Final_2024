from django.http import HttpResponse
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