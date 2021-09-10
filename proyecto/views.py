from django.http import HttpResponse
from django.template import Template, Context,loader


def informacion(request):
    #agregar integrantes del equipo.


    #cargar la plantilla usando el loader.


    #renderizar el documento externo(la plantilla) 
    
    documento = loader.get_template('plantilla.html')

    #enviar respuesta HttpResponse
    respuesta = documento.render({"lista_equipo":['Marcelo Plada', 'Gabriel Machado', 'Jorge Luis Scotti'], "titulo":'Proyecto final',"numero_equipo":3})
    
    return HttpResponse(respuesta)
    