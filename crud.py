from sqlalchemy.orm import Session 

import models, schemas 

def get_restaurant(db: Session, restaurant_id: int): 
  return db.query(models.Restaurant).filter(models.Restaurant.id== restaurant_id).first()

def get_restaurant_by_name(db: Session, name: str): 
  return db.query(models.Restaurant).filter(models.Restaurant.name== name).first()


def get_restaurants(db: Session, skip: int = 0, limit: int = 100): 
  return db.query(models.Restaurant).offset(skip).limit(limit).all()

def create_restaurant(db: Session, restaurant: schemas.RestaurantCreate): 
  fake_hashed_password = restaurant.password + "notreallyhashed"
  db_restaurant = models.Restaurant(name=restaurant.name, hashed_password = fake_hashed_password) 
  db.add(db_restaurant) 
  db.commit()
  db.refresh(db_restaurant)
  return db_restaurant 

def get_menu_items(db: Session, skip: int = 0, limit: int = 100):
  return db.query(models.MenuItem).offset(skip).limit(limit).all()


def create_restaurant_menu_item(db: Session, menu_item: schemas.MenuItemCreate, restaurant_id: int): 
  db_item = models.MenuItem(**menu_item.dict(), owner_id = restaurant_id) 
  db.add(db_item)
  db.commit()
  db.refresh(db_item)
  return db_item
