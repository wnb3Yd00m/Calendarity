from flask import Flask, render_template
from app import app
from .forms import EventForm

from app import db
from app.models import Event


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/make_event', methods=['post', 'get'])
def make_event():
    
    form = EventForm()
    if form.validate_on_submit():
        event_name = form.name.data
        event_start_time = form.start_time.data
        event_end_time = form.end_time.data
        event_description = form.description.data
        #print(event_description, event_end_time, event_name, event_start_time)
        
    return render_template('event.html', form=form)

@app.route('/events')
def events():
    events = Event.query.all()
    return str(events)