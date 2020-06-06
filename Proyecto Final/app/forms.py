from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, TextAreaField, BooleanField
from wtforms.validators import DataRequired, Email, Length

class SignupForm(FlaskForm):
	name = StringField('Nombre', validators=[DataRequired(), Length(max=64)])
	password = PasswordField('Password', validators=[DataRequired()])
	email = StringField('Email', validators=[DataRequired(), Email()])
	submit = SubmitField('Registrar')

class PostForm(FlaskForm):
	total = StringField('Total', validators=[DataRequired(), Length(max=64)])
	content = TextAreaField('Contenido')
	submit = SubmitField('Enviar')

class LoginForm(FlaskForm):
	email = StringField('Email', validators=[DataRequired()])
	password = PasswordField('Password', validators=[DataRequired()])
	remember_me = BooleanField('Recuérdame')
	submit = SubmitField('Login')

		
