from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"nombre": "Miguel Lopez"}

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