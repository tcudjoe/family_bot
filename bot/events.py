from db.models import session, Event

def add_event(member_name, description, event_date, event_time):
    event = Event(
        member_name=member_name,
        event_description=description,
        event_date=event_date,
        event_time=event_time
    )
    session.add(event)
    session.commit()
    return event

def get_events_for_date(date):
    return session.query(Event).filter(Event.event_date == date).all()
