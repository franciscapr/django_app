from django import forms

class EmailPostForm(forms.Form):
    name = forms.CharField(max_length=25)    # Nombre de la persona que enviara el post
    email = forms.EmailField()               # Correo electronico de la persona
    to = forms.EmailField()                  # Correo electronico del destinatario
    comments = forms.CharField(              # Comentario opcional 
        required=False,
        widget=forms.Textarea
    )