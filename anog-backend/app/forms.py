from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Length
    
class IndexForm(FlaskForm):
    user_input = StringField('user_input', validators=[DataRequired()])
    submit = SubmitField('Valider')
