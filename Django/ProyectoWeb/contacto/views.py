from ProyectoWeb.settings import EMAIL_HOST_USER
from django.shortcuts import redirect, render, redirect
from .forms import FormularioContacto

from django.core.mail import EmailMessage

# Create your views here.

def contacto(request):

    formulario_contacto = FormularioContacto()

    if request.method=="POST":
        formulario_contacto = FormularioContacto(data=request.POST) # Cargamos los datos en el formulario
        if formulario_contacto.is_valid(): # Si es válido, guardamos los datos
            nombre = request.POST.get("nombre")
            email = request.POST.get("email")
            contenido = request.POST.get("contenido")

            # Envío de e-mail

            email = EmailMessage("Mensaje desde !Django!",
                                "El usuario con nombre {} con la dirección {} escribe lo siguiente:\n\n{}".format(nombre, email, contenido),
                                EMAIL_HOST_USER,[EMAIL_HOST_USER], reply_to=[email]) # Primero va el emisor y luego el destinatario
            
            try:
                email.send()
                return redirect("/contacto/?valido") # Redirigimos transmitiendo el 'OK' del envío con GET
            except:
                return redirect("/contacto/?NOvalido") # Redirigimos transmitiendo el 'no OK' del envío con GET


    return render(request, "contacto/contacto.html", {'miFormulario':formulario_contacto})
