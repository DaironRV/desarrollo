from fastapi import FastAPI
from fastapi.responses import HTMLResponse


from config.database import engine,Base
from routers.product import product_router
from middlewares.error_handler import Errorhandler



app = FastAPI()
app.title = "Mi app con FastAPI"
app.version = "0.0.1"
app.include_router (product_router) 
app.add_middleware(Errorhandler)


Base.metadata.create_all(bind=engine)


@app.get('/',tags=['home'],status_code=200)
def message():
    return HTMLResponse('<h1>Hello Persona, no es la voz de tu cabeza es Dairon</h1>')

@app.get('/hola',tags=['home'])
def hola():
    return HTMLResponse('<h1>Hola persona con esquizofrenia</h1>')