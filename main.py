from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"nombre": "Miguel Lopez", "edad": 36}

@app.get("/users")
def list_users():
    return [
        {
           'name': 'Miguel Lopez Ariza',
           'email': 'lopezarizamiguel@gmail.com' 
        },
        {
           'name': 'Leo Lopez Ariza',
           'email': 'lopezarizaleo@gmail.com' 
        }
    ]

@app.get("/products")
def list_products():
    return [
        {
           'name': 'Pan de Sal',
        },
        {
           'name': 'Arina',
        }
    ]