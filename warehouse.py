#!/usr/bin/python
from collections import defaultdict

class Warehouse:
    
    def __init__(self):
        self.stock_quantities = defaultdict(int)
    
    def add(self, item_name, item_quantity):
        self.stock_quantities[item_name] += item_quantity
    
    def get_inventory(self, item_name):
        return self.stock_quantities[item_name]
    
    def has_inventory(self, item_name, item_quantity):
        return self.stock_quantities[item_name] >= item_quantity
    
    def remove(self, item_name, item_quantity):
        if self.has_inventory(item_name, item_quantity):
            self.stock_quantities[item_name] -= item_quantity
