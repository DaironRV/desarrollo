"product_service"


from models.product import Product as ProductModel 


class ProductService(): 
    def __init__(self, db): 
        self.db = db 

    def get_product(self): 
        result = self.db.query(ProductModel).all() 
        return result 

    def create_product(self, product: ProductModel): 
        new_product = ProductModel( 
            name=product.name.upper(), 
            brand=product.brand.upper(), 
            descripcion=product.descripcion.upper(), 
            price=product.price, 
            entry_date=product.entry_date 
        ) 
        self.db.add(new_product) 
        self.db.commit() 
        self.db.refresh 
        return 

    def get_for_id(self, id:int): 
        result = self.db.query(ProductModel).filter(ProductModel.id == id).first() 
        return result 

    def update_rating(self,data): 
        product = self.db.query(ProductModel).filter(ProductModel.id == data.id).first() 
        product.name = data.name 
        product.brand = data.brand 
        product.descripcion = data.descripcion 
        product.price = data.price 
        product.entry_date = data.entry_date 
        return 

    def delete_genre(self,id:int): 
        self.db.query(ProductModel).filter(ProductModel.id == id).delete() 
        self.db.commit() 
        return