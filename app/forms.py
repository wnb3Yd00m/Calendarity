from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Email

class EventForm(FlaskForm):
    name = StringField("Name ", validators=[DataRequired()])
    start_time = StringField("Event start time ", validators=[DataRequired()])
    end_time = StringField("Event end time ", validators=[DataRequired()])
    description = StringField("Description ")
    submit = SubmitField("Submit")