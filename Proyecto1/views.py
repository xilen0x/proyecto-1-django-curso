#-----------------Nuestras vistas del proyecto-------#

from django.http import HttpResponse
import datetime
from django.template import Template, Context

class Trabajador():
    def __init__(self, usuario, cargo, salario):
        self.usuario = usuario
        self.cargo = cargo
        self.salario = salario


# Dos instancias de la clase Trabajador
manager_tape = Trabajador("Ricardo","Manager",4000)
manager_Hub = Trabajador("Lilian","Manager",4800)


def saludo(request):
    #podemos usar variables y rescatarlos desde la plantilla:
    nombre = "Carlos"
    apellido = "Astorga"
    fecha_actual=datetime.datetime.now()
    #temas_curso = ["pyhton","django","base de datos","plantillas"]
    temas_curso = [] #si no tiene elementos, no entra al if de la plantilla
    #abrir la ruta del template
    doc_externo = open("plantillas/plantilla1.html")

    plt=Template(doc_externo.read())
    doc_externo.close()
    
    #creamos el contexto:
    #aqui le podemos pasar objetos de tipo clave:valor,estos pueden ser variables, clases utilizando el punto(ej.apellido, listas( "ej":["ele1","ele2","ele3"]))
    ctx=Context({"nombre_persona":nombre,
                "apellido_persona":apellido,
                "la_fecha":fecha_actual,
                "temas": temas_curso,   #aqui accedemos a la lista creada
                "clave_usuario1":manager_tape.usuario,"clave_cargo1":manager_tape.cargo,"clave_salario1":manager_tape.salario,
                "clave_usuario2":manager_Hub.usuario,"clave_cargo2":manager_Hub.cargo,"clave_salario2":manager_Hub.salario,
                }) #aqui accedemos a la clase creada

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