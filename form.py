from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class Form(FlaskForm):
    name = StringField('Имя', validators=[DataRequired()])
    data = StringField('Данные', validators=[DataRequired()])
    submit = SubmitField('Добавить')
