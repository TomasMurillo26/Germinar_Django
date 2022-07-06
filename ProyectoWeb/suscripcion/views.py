from msilib.schema import ListView
from multiprocessing import context
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views.generic import ListView
from .models import Membresia, Suscripcion, UserMembresia
from django.contrib import messages
# Create your views here.

def get_user_membership(request):
    userMembresia = UserMembresia.objects.filter(user=request.user)
    if userMembresia.exists():
        return userMembresia.first()
    return None

def get_user_subscription(request):
    suscripcion_user = Suscripcion.objects.filter(
        userMembresia = get_user_membership(request)
    )
    if suscripcion_user.exists():
        userSuscripcion = suscripcion_user.first()
        return userSuscripcion
    return None

def get_selected_membership(request):
    tipoMembresia = request.session['tipo_membresia_seleccionada']
    membresia_seleccionada_qs = Membresia.objects.filter(
        tipoMembresia = tipoMembresia
    )
    if membresia_seleccionada_qs.exists():
        return membresia_seleccionada_qs.first()
    return None




class ListaMembresia(ListView):
    model = Membresia

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        membresia_actual = get_user_membership(self.request)
        context['membresia_actual'] = str(membresia_actual.tipoMembresia)
        return context

    def post(self, request, **kwargs):
        tipo_membresia_seleccionada = request.POST.get('tipoMembresia')
        membresia_user = get_user_membership(request)
        suscripcion_user = get_user_subscription(request)
        membresia_seleccionada_qs = Membresia.objects.filter(
            tipoMembresia = tipo_membresia_seleccionada
        )
        if membresia_seleccionada_qs.exists():
            membresia_seleccionada = membresia_seleccionada_qs.first()

        if membresia_user.tipoMembresia == membresia_seleccionada:
            if suscripcion_user != None:
                messages.info(request, "Ya tienes esta membresía")
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

        request.session['tipo_membresia_seleccionada']=membresia_seleccionada.tipoMembresia

        return HttpResponseRedirect('confirmar')


def MembresiaView(request):
    membresia_user = get_user_membership(request)
    membresia_seleccionada = get_selected_membership(request)
    print(membresia_user)

    if request.method == "POST":
        try:
            membresia_user.tipoMembresia = membresia_seleccionada
            membresia_user.save()
            sub, created = Suscripcion.objects.get_or_create(UserMembresia=membresia_user)

        except:
            pass
    context = {
        'membresia_seleccionada': membresia_seleccionada
    }

    return render(request, "suscripcion/membresia_check.html", context)
