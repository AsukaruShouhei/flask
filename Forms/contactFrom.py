from flask_wtf import FlaskForm

from wtforms import Form, StringField, validators, SubmitField
from wtforms.validators import DataRequired

class MyForm(Form):
    name = StringField('name', validators=[DataRequired()])
    title = StringField('title', validators=[validators.Length(min=5)])
    message = StringField('message', validators=[DataRequired()])
    submit = SubmitField('送信')
