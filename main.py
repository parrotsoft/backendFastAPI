from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class User(BaseModel):
    email: str
    password: str



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
        },
        {
           'name': 'Alfredo Lopez M',
           'email': 'alfredo@gmail.com' 
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


@app.post("/login")
def login(dato: User):
    if (dato.email == 'miguel@test.com' and dato.password == '1234'):
        return {
            'status': 'success',
            'message': 'Datos correctos',
            'data': {
                'user_id': 1
            }
        }
    
    return {
        'status': 'error',
        'message': 'Si yaaaa!'
    }