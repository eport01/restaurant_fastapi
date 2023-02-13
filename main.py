from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session 
from mangum import Mangum

import crud, models, schemas
from database import SessionLocal, engine 

models.Base.metadata.create_all(bind=engine)
#use alembic

app = FastAPI()

# Dependency 
def get_db(): 
  db = SessionLocal()
  try: 
    yield db 
  finally: 
    db.close()


@app.post("/restaurants/", response_model=schemas.Restaurant, status_code=201)
def create_restaurant(restaurant: schemas.RestaurantCreate, db: Session = Depends(get_db)): 
  db_restaurant = crud.get_restaurant_by_name(db, name= restaurant.name )
  if db_restaurant: 
    raise HTTPException(status_code = 400, detail= "Restaurant already created")
  return crud.create_restaurant(db=db, restaurant=restaurant)

@app.get("/restaurants/", response_model=list[schemas.Restaurant])
def read_restaurants(skip: int=0, limit: int=100, db: Session = Depends(get_db)):
  restaurants = crud.get_restaurants(db, skip = skip, limit=limit)
  return restaurants 

@app.get("/restaurants/{restaurant_id}", response_model=schemas.Restaurant)
def read_restaurant(restaurant_id: int, db: Session = Depends(get_db)): 
  db_restaurant = crud.get_restaurant(db, restaurant_id=restaurant_id)
  if db_restaurant is None: 
    raise HTTPException(status_code = 404, detail= "Restaurant not found!")
  return db_restaurant 

@app.post("/restaurants/{restaurant_id}/menu_items/", response_model=schemas.MenuItem, status_code=201) 
def create_menu_item_for_restaurant(restaurant_id: int, menu_item: schemas.MenuItemCreate, db: Session = Depends(get_db)): 
  return crud.create_restaurant_menu_item(db, menu_item=menu_item, restaurant_id=restaurant_id)

@app.get("/menu_items/", response_model = list[schemas.MenuItem])
def read_menu_items(skip: int = 0, limit: int =100, db: Session = Depends(get_db)): 
  menu_items = crud.get_menu_items(db, skip=skip, limit=limit)
  return menu_items 

handler = Mangum(app=app)
