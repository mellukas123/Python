class Product:
    def __init__(self, name, price, category):
        self.name = name
        self.price = price
        self.category = category

    def __repr__(self):
        return f"Product(name={self.name}, price={self.price}, category={self.category})"

import random

class Customer:
    def __init__(self, name, has_loyalty_card):
        self.name = name
        self.basket = []
        self.has_loyalty_card = has_loyalty_card

    def add_product(self, product):
        self.basket.append(product)

    def __repr__(self):
        return f"Customer(name={self.name}, basket={self.basket}, has_loyalty_card={self.has_loyalty_card})"

class Cashier:
    def __init__(self, name):
        self.name = name

    def process_customer(self, customer, discounts):
        total_price = 0
        discounted_price = 0
        receipt = []

        for product in customer.basket:
            price = product.price
            discount = discounts.get(product.name, discounts.get(product.category, 0))
            discounted_price_item = price * (1 - discount)
            receipt.append({
                "product": product.name,
                "original_price": price,
                "discounted_price": discounted_price_item
            })
            total_price += price
            discounted_price += discounted_price_item

        return {
            "customer_name": customer.name,
            "products": receipt,
            "total_price": total_price,
            "total_discounted_price": discounted_price,
            "cashier_name": self.name
        }

    def __repr__(self):
        return f"Cashier(name={self.name})"

from collections import deque

class Queue:
    def __init__(self):
        self.customers = deque()

    def add_customer(self, customer):
        self.customers.append(customer)

    def next_customer(self):
        if self.customers:
            return self.customers.popleft()
        return None

    def __repr__(self):
        return f"Queue(customers={list(self.customers)})"

class Discount:
    def __init__(self, name, discount):
        self.name = name
        self.discount = discount

    def __repr__(self):
        return f"Discount(name={self.name}, discount={self.discount})"

import json

class Store:
    def __init__(self):
        self.products = []
        self.customers = []
        self.cashiers = []
        self.queue = Queue()
        self.discounts = {}

    def add_product(self, product):
        self.products.append(product)

    def add_customer(self, customer):
        self.customers.append(customer)

    def add_cashier(self, cashier):
        self.cashiers.append(cashier)

    def add_discount(self, name, discount):
        self.discounts[name] = discount

    def gather_products(self, customer):
        num_products = random.randint(1, 5)
        products = random.sample(self.products, num_products)
        for product in products:
            customer.add_product(product)

    def simulate_day(self):
        for customer in self.customers:
            self.gather_products(customer)
            self.queue.add_customer(customer)

        report = []
        while self.queue.customers:
            cashier = random.choice(self.cashiers)
            customer = self.queue.next_customer()
            customer_report = cashier.process_customer(customer, self.discounts)
            report.append(customer_report)

        with open('daily_report.json', 'w') as f:
            json.dump(report, f, indent=4)

        print("Simulation complete. Report generated.")

    def __repr__(self):
        return f"Store(products={self.products}, customers={self.customers}, cashiers={self.cashiers}, queue={self.queue}, discounts={self.discounts})"

# Create a store
store = Store()

# Add products
store.add_product(Product('Laptop', 1000, 'Electronics'))
store.add_product(Product('Smartphone', 800, 'Electronics'))
store.add_product(Product('TV', 500, 'Electronics'))
store.add_product(Product('Headphones', 100, 'Accessories'))
store.add_product(Product('Charger', 20, 'Accessories'))

# Add customers
store.add_customer(Customer('Laura', True))
store.add_customer(Customer('Karl', False))
store.add_customer(Customer('Merlyn', True))

# Add cashiers
store.add_cashier(Cashier('Anne'))
store.add_cashier(Cashier('Martin'))

# Add discounts
store.add_discount('Electronics', 0.1)  # 10% discount on all electronics
store.add_discount('Charger', 0.2)      # 20% discount on chargers

# Simulate a day in the store
store.simulate_day()
