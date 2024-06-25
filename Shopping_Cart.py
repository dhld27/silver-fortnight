'''
    =============================
    Shopping Cart Python Project

    this program made for add, remove, and preview in the shopping cart which consists of the exercise of OOPs and Functions code
    =============================
'''


class CartItem: 
    '''
    This Object indicates the item that wanted to be in the shopping cart 
    by adding the parameters name of the item and the price

    '''
    def __init__(self, name, price): 
        self.name = name
        self.price = price

    def __str__(self): 
        return f'{self.price}: {self.name}'

class ShoppingCart:
    '''
    This Object indicates the Cart following 
    by some functions that can be edit while the program is running

    '''
    def __init__(self):
        self.items = []
    
    def addItem(self, item):
        '''
        This Function shows the works of adding item based on 'Class' Object above. 

        '''
        if not isinstance(item, CartItem):
            '''
            Exception handling, if it's an invalid item, it will rase a ValueError with an error message
        
            '''
            raise ValueError ('Item is not available')
        self.items.append(item)
        
    def removeItem (self, item): 
        '''
        This Function shows how to remove item based on 'Class' Object above.
        
        ''' 
        for i in self.items:
            if item == i.name:
                self.items.remove(i)
                print('The item has been removed.')

    def calculateItemsTotal (self): 
        '''
        This Function indicates the total of the price based on 'Class' Object above, from the second parameter.
        
        '''
        total = sum(item.price for item in self.items)
        return total
    
    def displayItem (self): 
        '''
        This Function indicates the display of numbers of items that user already input.
        
        '''
        if not self.items:
            print('Empty item in the cart.')
        else:
            print('The item(s) in the cart: ')
            for item in self.items:
                print(f'{item.name}: €.{item.price}')

    def userInterface (self): 
        '''
        This is where the display of the menu is shown, following by the mechanism of each options that consists of conditional operations

        '''
        
        while True:
            '''
            Using While Looping is because user can decided whether they want to add, remove, show the item(s), and show the price as long as they want.
            
            '''
            print('\tWelcome to Lidl Supermarkt.')
            print('')
            print('\tMain Menu :')
            print('')
            print('1. Add Item')
            print('2. Remove Item')
            print('3. Show Item(s) in the cart')
            print("4. Show Item's price ")
            print('5. Exit')

            option = input('Choose the menu: ')

            if option == '1': 
                '''
                If user choose this number, it leads to input the item name and the price, once successfully added, it'll show message "the item has been added"
                
                '''
                name = input('Enter the Item: ')
                price = int(input("Enter the price: "))
                item = CartItem(name, price)
                self.items.append(item)
                print('the item has been added')

            elif option == '2': 
                '''
                If user choose this number(after add an item), it leads to input the item name, once successfully added, it'll show message "the item has been removed"
                
                '''
                itemName = input('Please enter the item you want to remove: ')
                self.removeItem(itemName)
            
            elif option == '3': 
                '''
                If user choose this number(after add an item or some items), it'll show the list of the added item(s)
                                
                '''
                self.displayItem()
            
            elif option == '4': 
                '''
                If user choose this number(after add an item or some items), it'll show the list of the added items following by the price and the total price
                
                '''
                itemsPrice = self.calculateItemsTotal()
                for item in self.items:
                    print(f'{item.name}: €.{item.price}')
                print(f'Total : €. {itemsPrice}')
        
            elif option == '5': 
                '''
                If user wants to stop the program, the user can choose this number that indicates the program is done being used.
                
                '''
                print('Thank you for using our program!')
                break
            else: 
                print('The option is unavailable.')


if __name__ == '__main__':
    shopping_cart = ShoppingCart()
    shopping_cart.userInterface()