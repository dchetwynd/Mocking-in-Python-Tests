#!/usr/bin/python
from warehouse import Warehouse

class Order:
    
    def __init__(self, item_name, item_quantity):
        self.item_name = item_name
        self.item_quantity = item_quantity
        self.is_filled = False
    
    def fill(self, warehouse):
        if warehouse.has_inventory(self.item_name, self.item_quantity):
            self.is_filled = True
            warehouse.remove(self.item_name, self.item_quantity)
