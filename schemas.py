from pydantic import BaseModel 

class MenuItemBase(BaseModel): 
  name: str 
  description: str | None = None 

class MenuItemCreate(MenuItemBase):
  pass 

class MenuItem(MenuItemBase): 
  id: int 
  owner_id: int 

  class Config: 
    orm_mode= True 

class RestaurantBase(BaseModel): 
  name: str 

class RestaurantCreate(RestaurantBase): 
  password: str 

class Restaurant(RestaurantBase): 
  id: int 
  # is_active: bool 
  menu_items: list[MenuItem] = []

  class Config: 
    orm_mode = True 