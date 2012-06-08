#!/usr/bin/python
from mock import MagicMock, call
from order import *
from warehouse import *
import unittest

class OrderTest(unittest.TestCase):
    
    def testWarehouseStockRemovedWhenSufficientStockAvailableForOrder(self):
        o = Order("milk", 20)
        w = Warehouse()
        w.add("milk", 30)
        
        o.fill(w)
        self.assertEqual(10, w.get_inventory("milk"))
    
    def testWarehouseStockNotRemovedWhenInsufficientStockAvailableForOrder(self):
        o = Order("milk", 20)
        w = Warehouse()
        w.add("milk", 15)
        
        o.fill(w)
        self.assertEqual(15, w.get_inventory("milk"))
    
    def testOrderIsFilledForSufficientStockInWarehouse(self):
        o = Order("milk", 20)
        w = MagicMock(spec=Warehouse)
        w.has_inventory.return_value = True
        
        o.fill(w)
        self.assertEqual(True, o.is_filled)
    
    def testOrderIsNotFilledForInsufficientStockInWarehouse(self):
        o = Order("milk", 20)
        w = MagicMock(spec=Warehouse)
        w.has_inventory.return_value = False
        
        o.fill(w)
        self.assertEqual(False, o.is_filled)
    
    def testFillingOrderChecksTheWarehouseInventory(self):
        o = Order("milk", 20)
        w = MagicMock(spec=Warehouse)
        
        o.fill(w)
        self.assertEqual(True, w.has_inventory.called)
    
    def testFillingOrderRemovesWarehouseItemsWhenSufficientStockIsAvailable(self):
        o = Order("milk", 20)
        w = MagicMock(spec=Warehouse)
        w.has_inventory.return_value = True
        
        o.fill(w)
        self.assertEqual(True, call.remove("milk", 20) in w.mock_calls)
        
if __name__ == '__main__':
    unittest.main()
