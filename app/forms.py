from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.fields.html5 import DateField, TimeField
from wtforms.validators import DataRequired, Email

class EventForm(FlaskForm):
    name = StringField("Event name", validators=[DataRequired()])
    start_time = TimeField("Event start time", validators=[DataRequired()])
    end_time = TimeField("Event end time", validators=[DataRequired()])
    start_date = DateField("Event start date", validators=[DataRequired()])
    end_date = DateField("Event end date", validators=[DataRequired()])
    description = TextAreaField("Description ")
    submit = SubmitField("Submit")