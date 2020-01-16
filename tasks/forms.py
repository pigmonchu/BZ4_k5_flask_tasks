from flask_wtf import FlaskForm
from wtforms import StringField, DateField, SubmitField, HiddenField
from wtforms.validators import DataRequired, Length, ValidationError, AnyOf, Email
from wtforms.widgets import TextArea

from datetime import date

def greater_than_today(form, field):
    hoy = date.today()
    if field.data < hoy:
        raise ValidationError('La fecha debe ser superior o igual a hoy')


class TaskForm(FlaskForm):
    title = StringField('Título', validators=[DataRequired(), Length(min=3, max=15, message="La longitud ha de estar entre 3 y 15")])
    description = StringField('Descripción', widget=TextArea())
    fx = DateField('Fecha', validators=[DataRequired(), greater_than_today])

    submit = SubmitField('Enviar')

class ProccesTaskForm(FlaskForm):
    ix = HiddenField('ix', validators=[DataRequired()])
    btn = HiddenField('btn', validators=[DataRequired(), AnyOf(['M', 'B'])])
    title = StringField('Título', validators=[DataRequired(), Length(min=3, max=15, message="La longitud ha de estar entre 3 y 15")])
    description = StringField('Descripción', widget=TextArea())
    fx = DateField('Fecha', validators=[DataRequired()])

    submit = SubmitField('Aceptar')

class EmployeeForm(FlaskForm):
    name = StringField('Nombre', validators=[DataRequired()])
    lastname = StringField('Apellidos', validators=[DataRequired()])
    email = StringField('Correo electrónico', validators=[DataRequired(), Email()])

    submit = SubmitField('Enviar')

class ProccessEmployeeForm(FlaskForm):
    id = HiddenField('id', validators=[DataRequired()])
    btn = HiddenField('btn', validators=[DataRequired(), AnyOf(['M', 'B'])])
    name = StringField('Nombre', validators=[DataRequired()])
    lastname = StringField('Apellidos', validator=[DataRequired()])
    email = StringField('Correo electrónico', validator=[DataRequired(), Email()])

    submit = SubmitField('Aceptar')
