#-----------------Nuestras vistas del proyecto-------#

from django.http import HttpResponse
import datetime
from django.template import Template, Context

def saludo(request):
    #abrir la ruta del template
    doc_externo = open("plantillas/plantilla1.html")

    plt=Template(doc_externo.read())
    doc_externo.close()
    #creamos el contexto(en este caso esta vacio):
    ctx=Context()
    documento = plt.render(ctx)

    return HttpResponse(documento)

def despedida(request):
    return HttpResponse("Hasta pronto!")

def fecha(request):
    fecha_actual=datetime.datetime.now()

    return HttpResponse("<h2>Fecha y hora actual %s</h2>" % fecha_actual)

def calculaEdad(request, edad, anio):
    #edadActual=45
    periodo = anio-2021
    edadFutura = edad + periodo
    documento = "<h2>En el año %s tendrás %s años.</h2>" %(anio, edadFutura)

    return HttpResponse(documento)