from sqlalchemy import Boolean, Column, ForeignKey, Integer, String 
from sqlalchemy.orm import relationship 

from database import Base 

class Restaurant(Base): 
  __tablename__= 'restaurants' 
  id = Column(Integer, primary_key=True, index=True)
  name = Column(String, unique=True, index=True)
  email = Column(String, unique=True, index=True)
  hashed_password = Column(String)  
  description = Column(String, default=True)

  menu_items = relationship("MenuItem", back_populates="owner")

class MenuItem(Base): 
  __tablename__ = 'menu_items'  

  id = Column(Integer, primary_key=True, index=True)
  name = Column(String, index=True)
  description = Column(String, index=True)  
  tags = Column(String, index=True)  
  category = Column(String, index=True)  
  image = Column(String, index=True)  
  price = Column(Integer, index=True)  

  owner_id = Column(Integer, ForeignKey("restaurants.id"))

  owner = relationship("Restaurant", back_populates="menu_items")