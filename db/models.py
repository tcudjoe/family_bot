from sqlalchemy import create_engine, Column, Integer, String, Date, Time
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()
engine = create_engine("sqlite:///family_bot.db")
Session = sessionmaker(bind=engine)
session = Session()

class Event(Base):
    __tablename__ = "events"
    id = Column(Integer, primary_key=True)
    member_name = Column(String, nullable=False)
    event_description = Column(String, nullable=False)
    event_date = Column(Date, nullable=False)
    event_time = Column(Time, nullable=False)

Base.metadata.create_all(engine)
