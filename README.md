<div align="center">
  <h1>Restaurants API</h1>
  <div align="center"><img src="images/food_photo.jpeg" alt="Deschutes Brewery GIF" class="center" width="480" height="320"></div>
</div>

<br>

# Developer Setup
  1. Make sure to have [Python](https://www.python.org/downloads/) Locally.
  2. Clone the repository 
  3. ```cd``` into the root directory 
  4. Create virtual environment ```python3 -m venv env```  
  5. Activate virtual environment ```source ./env/bin/activate```
  6. To install requirements run: ```pip3 install -r requirements.txt ```
  7. To view endpoints locally run: ```uvicorn main:app --reload``` and navigate to url listed in terminal i.e. ```http://127.0.0.1:8000```
  8. You can view the interactive docs by adding ```/docs``` to the url in step 5 