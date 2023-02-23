import email
from django.shortcuts import redirect, render

from .forms import FormularioContacto
from django.core.mail import EmailMessage

# Create your views here.



def contacto(request):

   formulario_contacto = FormularioContacto()

   if request.method == "POST":
      formulario_contacto = FormularioContacto(data = request.POST)
      if formulario_contacto.is_valid():
         nombre = request.POST.get("nombre")
         email = request.POST.get("email")
         mensaje = request.POST.get("mensaje")


         email = EmailMessage("Mensaje desde APP Django",
         "El usuario {}, direccion {}, te dice:\n\n {}".format(nombre,email,mensaje),
         "",["lajaragames@gmail.com"],reply_to=[email])

         try:
            email.send()
            return redirect("/contacto/?valido")
         except:
            return redirect("/contacto/?error")

   return render(request, "contacto/contacto.html", {'miFormulario': formulario_contacto})