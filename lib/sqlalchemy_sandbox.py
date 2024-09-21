# lib/sqlalchemy_sandbox.py
#!/usr/bin/env python3
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    pass


class Student(Base):
    __tablename__ = "students"

    id = Column(Integer(), primary_key=True)
    name = Column(String())


engine = create_engine("sqlite:///../students.db")
Base.metadata.create_all(engine)
