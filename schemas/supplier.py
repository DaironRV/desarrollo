from pydantic import BaseModel, Field
from typing import Optional


class Supplier(BaseModel):
    id : Optional[int] = None
    name : str=Field(max_length=40, min_length=40, description="supplier name")
    address : str=Field(max_length=40, max_items=40, description= "address")
    phone : int=Field(ge=10, le= 10)
    email : str=Field(max_length=40, min_length=10, description= "email supplier")


    class Config:
        schema_extra = {
            'example':{
                'id': 1,
                'name': 'Ramo',
                'address':'Carrera 27 a No. 68_50 Barrio Alcázares',
                'phone': 14375700,
                'email': 'seleccion@www.ramo.com.co, is the closest thing to an email that I found'
            } 
        }