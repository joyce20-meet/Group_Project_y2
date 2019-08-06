
from model import Base, Volunteer

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///lecture.db?check_same_thread=False')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()
def add_event(name,chosen_event):
	volunteer_object = Volunteer(
		username = name,
		event=chosen_event)
	session.add(volunteer_object)
	session.commit()
def query_all():
	volunteers = session.query(Volunteer).all()
	return volunteers
