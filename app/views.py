from flask import Flask, render_template
from app import app, db
from .forms import EventForm
from app.models import Event

from datetime import date


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
        event_description = form.description.data
        
        start_time = event_start_time.split('.')
        start_year = int(start_time[0])
        start_month = int(start_time[1])
        start_day = int(start_time[2])
        
        end_time = event_end_time.split('.')
        end_year = int(end_time[0])
        end_month = int(end_time[1])
        end_day = int(end_time[2])
        
        u = Event(name=event_name, start_time=date(start_year, start_month, start_day), end_time=date(end_year, end_month, end_day), description=event_description)
        db.session.add(u)
        db.session.commit()
        #print(event_description, event_end_time, event_name, event_start_time)
        
    return render_template('event.html', form=form)

@app.route('/events')
def events():
    events = Event.query.all()
    #result = ''
    #for event in events:
    #    result += str(event.id) + ' ' + event.name + ' ' + str(event.start_time) + ' ' + str(event.end_time) + ' ' + event.description + "<br>"
    return render_template('show_events.html', events=events) #, result=result)