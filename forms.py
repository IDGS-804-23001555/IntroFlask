from wtforms import Form, validators
from wtforms import StringField, PasswordField, EmailField,BooleanField, IntegerField

class Userform(Form):
    matricula= IntegerField("Matricula", [validators.DataRequired(message="Este campo es requerido")])
    nombre= StringField("Nombre", [validators.DataRequired(message="Este campo es requerido")])
    apellido= StringField("Apellido", [validators.DataRequired(message="Este campo es requerido")])
    correo= EmailField("Correo", [validators.Email(message="ingrese un correo valido")])