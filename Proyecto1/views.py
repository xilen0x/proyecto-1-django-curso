#-----------------Nuestras vistas del proyecto-------#

from django.http import HttpResponse
import datetime
from django.template import Template, Context
from django.template.loader import get_template
from django.shortcuts import render

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
    nombre = "CarlosRRRR"
    apellido = "Astorga"
    fecha_actual=datetime.datetime.now()
    #temas_curso = ["pyhton","django","base de datos","plantillas"]
    temas_curso = [] #si no tiene elementos, no entra al if de la plantilla
    #abrir la ruta del template (las sgtes. 3 lineas se han comentado pq utlizare en su lugar el cargador de templates loader)
    #doc_externo = open("plantillas/plantilla1.html")
    #plt=Template(doc_externo.read())
    #doc_externo.close()
    
    #doc_externo = loader.get_template('plantilla1.html')
    #doc_externo = get_template('plantilla1.html') #podemos prescindir del loader, ya q esta importado arriba.

    #creamos el contexto:
    #aqui le podemos pasar objetos de tipo clave:valor,estos pueden ser variables, clases utilizando el punto(ej.apellido, listas( "ej":["ele1","ele2","ele3"]))
    """ ctx=Context({"nombre_persona":nombre,
                "apellido_persona":apellido,
                "la_fecha":fecha_actual,
                "temas": temas_curso,   #aqui accedemos a la lista creada
                "clave_usuario1":manager_tape.usuario,"clave_cargo1":manager_tape.cargo,"clave_salario1":manager_tape.salario,
                "clave_usuario2":manager_Hub.usuario,"clave_cargo2":manager_Hub.cargo,"clave_salario2":manager_Hub.salario,
                })  """#aqui accedemos a la clase creada

#El otro método de realizar lo mismo pero mas profesional, es con un cargador de plantillas. Dentro del archivo settings.py ponemos la ruta de la carpeta con nuestra plantillas(en TEMPLATES->'DIRS': ['path/'] )
#Aquí el método render acepta directamente el diccionario y no a traves de un contexto como en el caso anterior #comentado
    """ documento = doc_externo.render({"nombre_persona":nombre,"apellido_persona":apellido,"la_fecha":fecha_actual,"temas": temas_curso, "clave_usuario1":manager_tape.usuario,"clave_cargo1":manager_tape.cargo,"clave_salario1":manager_tape.salario,"clave_usuario2":manager_Hub.usuario,"clave_cargo2":manager_Hub.cargo,"clave_salario2":manager_Hub.salario, }) """

    diccionario = {"nombre_persona":nombre,"apellido_persona":apellido,"la_fecha":fecha_actual,"temas": temas_curso, "clave_usuario1":manager_tape.usuario,"clave_cargo1":manager_tape.cargo,"clave_salario1":manager_tape.salario,"clave_usuario2":manager_Hub.usuario,"clave_cargo2":manager_Hub.cargo,"clave_salario2":manager_Hub.salario, }
    #return HttpResponse(documento)
    return render(request, "plantilla1.html", diccionario)




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

def curso_django(request):
    fecha_actual=datetime.datetime.now()
    return render(request, "plantilla_hija.html", {"fecha":fecha_actual})

def curso_js(request):
    fecha_actual=datetime.datetime.now()
    return render(request, "plantilla_hija2.html", {"fecha":fecha_actual})