from fastapi import APIRouter
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from service.supplier import SupplierService
from config.database import Session
from schemas.supplier import Supplier

supplier_router = APIRouter()


@supplier_router. get('/supplier',tags=['product'], status_code= 200)
def get_supplier():
    db = Session()
    result = SupplierService(db).get_for_id(id)
    return JSONResponse(content= jsonable_encoder(result), status_code=200)

@supplier_router.get ('supplier_for:id', tags=['supplier'], status_code=200)
def get_supplier_for_id(id:int):
    db = Session()
    result = SupplierService(db). get_for_id(id)
    return JSONResponse (content= jsonable_encoder(result), status_code= 200)

@supplier_router. post('/supplier', tags=['supplier'], status_code= 201)
def cerate_supplier(supplier:Supplier):
    db = Session()
    SupplierService(db). create_supplier(supplier)
    return JSONResponse (content={'message':'supplier create succesfully', 'status_code':200}, status_code= 201)

@supplier_router.put ('/supplier{id}', tags=['supplier'])
def update_supplier(id:int, data:Supplier):
    db = Session()
    result = SupplierService(db).get_for_id(id)
    if not result:
        return JSONResponse(content={'message':'supplier update successfully', 'status_code':200}, status_code= 200)
    SupplierService(db).update_supplier(data)
    return JSONResponse (content={'message':'supplier update successfully', 'status_code':404})

@supplier_router.delete('/supplier{id}', tags=['supplier'])
def delete_supplier(id:int):
    db = Session()
    result = SupplierService(db).get_for_id(id)
    if not result:
        return JSONResponse(content={'message':"supplies don't found", 'status_code':404})
    SupplierService(db).delete_supplier(id)
    return JSONResponse (content={'menssage':'supplier update succesfully', 'status_code':200}, status_code=200)