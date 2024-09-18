from django.forms import modelform_factory
from django.shortcuts import render, get_object_or_404, redirect

from personas.models import Persona


# Create your views here.
def detalle_persona(request, id):
    # persona = Persona.objects.get(pk=id)
    persona = get_object_or_404(Persona, pk=id)  # Devuelve un 404 si no existe
    return render(request, 'detalle_persona.html', {'persona': persona})


# Create a form from a model
PersonaForm = modelform_factory(Persona, exclude=[])


def nueva_persona(request):
    if request.method == 'POST':
        form = PersonaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = PersonaForm()
    return render(request, 'nueva_persona.html', {'form': form})


def editar_persona(request, id):
    persona = get_object_or_404(Persona, pk=id)
    if request.method == 'POST':
        form = PersonaForm(request.POST, instance=persona)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = PersonaForm(instance=persona)
    return render(request, 'editar_persona.html', {'form': form})


def eliminar_persona(request, id):
    persona = get_object_or_404(Persona, pk=id)
    if request.method == 'POST':
        persona.delete()
        return redirect('index')
    return render(request, 'eliminar_persona.html', {'persona': persona})
