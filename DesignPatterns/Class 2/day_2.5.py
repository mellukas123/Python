class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

# you can implement just product factory
class ProductFactory:
    def create_product(self, name, price):
        return Product(name, price)

# OR you can make factory for making factories! :)
class FactoryFactory:
    def create_factory(self, product_class):
        class Factory:
            def create_product(self, name, price):
                return product_class(name, price)
        return Factory()

# creating the factory of factories
factory_factory = FactoryFactory()

# creating the factory of products
product_factory = factory_factory.create_factory(Product)

# creating products through the product factory
product1 = product_factory.create_product("Product A", 10.0)
product2 = product_factory.create_product("Product B", 20.0)

print(f"{product1.name}: {product1.price}")
print(f"{product2.name}: {product2.price}")


Message design-patterns

