'supplier_service'

from models.supplier import Supplier as SupplierModel


class SupplierService():
    def __init__(self,db):
        self.db = db

    def get_supplier(self):
        result = self.db.query(SupplierModel).all()
        return result 

    def create_supplier(self, supplier: SupplierModel):
        new_supplier= SupplierModel(
            name= supplier.name.upper(),
            address= supplier.address.upper(),
            phone= supplier.phone.upper(),
            email= supplier.email.upper()
        )
        self.db.add(new_supplier)
        self.db.commint()
        self.db.refresh
        return

    def get_for_id(self, id:int):
        result = self.db.query(SupplierModel)
        return result

    def update_rating(self,data):
        supplier = self.db.query(SupplierModel).filter(SupplierModel.id == data.id).frist()
        supplier.name = data.name
        supplier.address = data.address
        supplier.phone = data.phone
        supplier.email = data.email
        supplier.entry_date = data.entry_date
        return

    def delete_genre(self,id:int):
        self.db.query(SupplierModel).filter(SupplierService.id == id).delete()
        return