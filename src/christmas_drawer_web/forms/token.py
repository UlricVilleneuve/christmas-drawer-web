from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class TokenForm(FlaskForm):
    token = StringField('Token', validators=[DataRequired()])
    submit = SubmitField('Entrer')
