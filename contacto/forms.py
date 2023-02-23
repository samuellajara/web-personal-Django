from django import forms

class FormularioContacto(forms.Form):

    nombre = forms.CharField(label = "Nombre", required = True, max_length = 20)
    email = forms.EmailField(label = "Email", required = True, max_length = 50)
    mensaje = forms.CharField(label = "Mensaje", required = True, widget = forms.Textarea)

    