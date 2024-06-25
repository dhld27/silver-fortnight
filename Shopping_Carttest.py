import unittest
from Shopping_Cart import CartItem, ShoppingCart

class testCartItem (unittest.TestCase):
    def setUp(self):
        self.lidl = ShoppingCart()

    def testaddItem(self): 
        '''
        This function is testing whether the add item function from Shopping_Cart.py is matching the program workflow
        
        '''
        item1 = CartItem('Lidl Nugget', 15000)
        self.lidl.addItem(item1)
        self.assertEqual(len(self.lidl.items), 1)

    def testremoveItem(self): 
        '''
        This function is testing whether the added item 
        can be removed by the remove function from Shopping_Cart.py is matching the program workflow
        
        '''
        item2 = CartItem('Lidl Nugget', 15000)
        item3 = CartItem('Milch Schokolade', 10000)
        self.lidl.addItem(item2)
        self.lidl.addItem(item3)
        self.lidl.removeItem('Lidl Nugget')
        self.assertEqual(len(self.lidl.items), 1)
    
    def testcalculateItems(self): 
        '''
        This function is testing whether the price from the added item 
        can be calculate to total of how much items has been added with the price.
        
        '''
        item2 = CartItem('Lidl Nugget', 15000)
        item3 = CartItem('Milch Schokolade', 10000)
        self.lidl.addItem(item2)
        self.lidl.addItem(item3)
        self.assertEqual(self.lidl.calculateItemsTotal(), 25000)

if __name__ == '__main__':
    unittest.main()