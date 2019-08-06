from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine
Base = declarative_base()
class Volunteer(Base):
	__tablename__ ="Volunteer"
	user_id = Column(Integer,primary_key=True)
	username = Column(String)
	phonenumber = Column(String)
	event = Column(String)
	def __repr__(self):
		return("volunteer_name: {}\n"
				"Volunteer_choice: {}\n"
				"Volunteer_phonenumber").format(
				self.username,
				self.event,
				self.phonenumber)
			