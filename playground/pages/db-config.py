from sqlalchemy import Column, Integer, String, Date, Enum, Text, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    user_id = Column(Integer, primary_key=True)
    username = Column(String(50), nullable=False, unique=True)
    email = Column(String(100), nullable=False, unique=True)
    password = Column(String(100), nullable=False)
    auth_token = Column(String(100))

class UserData(Base):
    __tablename__ = 'user_data'

    data_id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.user_id'), nullable=False)
    full_name = Column(String(100))
    bio = Column(Text)

    user = relationship("User", back_populates="user_data")
