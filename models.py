import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, \
    DateTime, Time, Boolean, Interval
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine


Base = declarative_base()


class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    picture = Column(String(250))


class Meal(Base):
    __tablename__ = 'meal'

    id = Column(Integer, primary_key=True)
    created = Column(DateTime)
    description = Column(String(250))
    duration = Column(Interval, nullable=False)
    start_time = Column(DateTime)
    end_time = Column(DateTime)
    healthy = Column(Boolean, default=True)
    unhealthy = Column(Boolean, default=False)
    starch_rich = Column(Boolean, default=False)
    sucrose_rich = Column(Boolean, default=False)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)

    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            'id': self.id,
            'healthy': self.healthy,
            'unhealthy': self.unhealthy,
            'starch_rich': self.starch_rich,
            'sucrose_rich': self.sucrose_rich,
            'duration': self.duration,
            'start_time': self.start_time,
            'end_time': self.end_time
        }


class Sleep(Base):
    __tablename__ = 'sleep'

    id = Column(Integer, primary_key=True)
    created = Column(DateTime)
    duration = Column(Interval, nullable=False)
    start_time = Column(DateTime)
    end_time = Column(DateTime)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)

    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            'id': self.id,
            'duration': self.duration
        }


class Workout(Base):
    __tablename__ = 'workout'

    id = Column(Integer, primary_key=True)
    created = Column(DateTime)
    duration = Column(Interval, nullable=False)
    start_time = Column(DateTime)
    end_time = Column(DateTime)
    intense = Column(Boolean, default=False)
    light = Column(Boolean, default=True)
    interval = Column(Boolean, default=False)
    endurance = Column(Boolean, default=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)

    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            'id': self.id,
            'duration': self.duration,
            'type': self.type,
            'intense': self.intense,
            'light': self.light,
            'interval': self.interval,
            'endurance': self.endurance
        }


class Weight(Base):
    __tablename__ = 'weight'

    id = Column(Integer, primary_key=True)
    created = Column(DateTime)
    weight = Column(Integer, nullable=False)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)

    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            'id': self.id,
            'weight': self.weight
        }


class BloodPressure(Base):
    __tablename__ = 'blood_pressure'

    id = Column(Integer, primary_key=True)
    created = Column(DateTime)
    systolic = Column(Integer, nullable=False)
    diastolic = Column(Integer, nullable=False)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)

    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            'id': self.id,
            'systolic': self.systolic,
            'diastolic': self.diastolic
        }


class BloodSugar(Base):
    __tablename__ = 'blood_sugar'

    id = Column(Integer, primary_key=True)
    created = Column(DateTime)
    glucose_level = Column(Integer, nullable=False)
    insulin_level = Column(Integer, nullable=False)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)

    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            'id': self.id,
            'datetime': self.datetime,
            'glucose_level': self.glucose_level,
            'insulin_level': self.insulin_level
        }


class HeartRate(Base):
    __tablename__ = 'heart_rate'

    id = Column(Integer, primary_key=True)
    created = Column(DateTime)
    bpm = Column(Integer, nullable=False)
    resting = Column(Boolean, nullable=False)
    active = Column(Boolean, nullable=False)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)

    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            'id': self.id,
            'bpm': self.name,
            'resting': self.resting,
            'active': self.active
        }


engine = create_engine('sqlite:///healthdata.db')


Base.metadata.create_all(engine)
