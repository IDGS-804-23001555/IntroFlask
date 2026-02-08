from wtforms import Form
from wtforms import StringField, IntegerField, RadioField
from wtforms import validators


class CinepolisForm(Form):
    nombre = StringField('Nombre',[validators.DataRequired(message='El nombre es requerido')])
    cant_compradores = IntegerField('Cantidad Compradores',[
            validators.DataRequired(message='Campo requerido'),
            validators.NumberRange(min=1, message='Debe haber al menos 1 comprador')])
    cant_boletas = IntegerField('Cantidad de Boletas',[
            validators.DataRequired(message='Campo requerido'),
            validators.NumberRange(min=1, message='Debe comprar al menos 1 boleta')])
    tarjeta = RadioField('Tarjeta Cineco',
        choices=[('Si', 'Si'), ('No', 'No')],
        default='No')