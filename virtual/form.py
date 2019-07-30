from flask_wtf import FlaskForm
from wtforms import SubmitField,StringField,RadioField,PasswordField,TextAreaField,IntegerField,HiddenField
from wtforms.validators import DataRequired,Optional, Length
from wtforms_components import EmailField
from wtforms.widgets.html5 import NumberInput
from flask_babel import Babel


class formulario(FlaskForm):
    tipo = "cadastro"
    cod = HiddenField()
    nome = StringField('Nome',validators=[DataRequired()])
    login = StringField('login',validators=[DataRequired()])
    altura = StringField('altura',validators=[DataRequired()])
    senha = PasswordField('Senha',validators=[DataRequired()])
    idade = IntegerField('Idade',validators=[DataRequired()])
    email =  EmailField('Email',validators=[DataRequired()])
    enviar = SubmitField('Enviar')