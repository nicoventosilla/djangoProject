from django.shortcuts import render

from personas.models import Persona


# Create your views here.
def index(request):
    numero_personas = Persona.objects.count()
    # personas = Persona.objects.all()
    personas = Persona.objects.order_by('id')
    return render(request, 'index.html', {'numero_personas': numero_personas, 'personas': personas})
