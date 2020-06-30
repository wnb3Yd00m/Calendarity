from flask import Flask, render_template
from app import app, db
from .forms import EventForm
from app.models import Event

import datetime


@app.route('/')
def hello_world():
    return render_template('index.html')


@app.route('/make_event', methods=['post', 'get'])
def make_event():
    
    form = EventForm()
    if form.validate_on_submit():
        event_name = form.name.data
        event_start_time = form.start_time.data
        event_end_time = form.end_time.data
        event_start_date = form.start_date.data
        event_end_date = form.end_date.data
        event_description = form.description.data
        
        event_start_full_time = datetime.datetime.combine(event_start_date, event_start_time)
        event_end_full_time = datetime.datetime.combine(event_end_date, event_end_time)

        u = Event(name=event_name, start_time=event_start_full_time, end_time=event_end_full_time, description=event_description)
        db.session.add(u)
        db.session.commit()
        # print(event_name, ' ', type(event_name), '\n', \
            #   event_start_time, type(event_start_time), '\n', \
            #   event_start_date, type(event_start_date), '\n', \
            #   event_end_time, type(event_end_time), '\n', \
            #   event_end_date, type(event_end_date), '\n', \
            #   event_description,)
        
    return render_template('event.html', form=form)

@app.route('/events')
def events():
    events = Event.query.all()
    #result = ''
    #for event in events:
    #    result += str(event.id) + ' ' + event.name + ' ' + str(event.start_time) + ' ' + str(event.end_time) + ' ' + event.description + "<br>"
    return render_template('show_events.html', events=events) #, result=result)