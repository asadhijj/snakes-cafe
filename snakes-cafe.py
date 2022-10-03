def items() :
    
    while True:
        item = input ('> ').title()
        if item.lower() == 'quit':
            
            print ("Thank you for visiting us")
            break
        if item in menu : 
            menu[item]+=1
            if menu[item]==1 :
                print (f"1 order of {item} have been added to your meal")
                
            else : 
                 print (f" {menu[item]} orders of {item} have been added to your meal")
                    
        else : 
             print ("the item is not available")
        
    
print ('''
*******************************************
**      Welcome to the snakes cafe      **
**      Please See Our menue below      **
**                                      **
**   To quit at any time, type "quit"   **
*******************************************
''')

print ('''
Appetizers
----------
Wings
Cookies
Spring Rolls
Entrees
-------
Salmon
Steak
Meat Tornado
A Literal Garden
Desserts
--------
Ice Cream
Cake
Pie
Beverages
------
Coffee
Tea
Unicorn Tears
***********************************
** What would you like to order? **
***********************************
''')
menu = {
    "Wings": 0,
    "Cookies": 0,
    "Spring Rolls": 0,
    "Salmon": 0,
    "Steak": 0,
    "Meat Tornado": 0,
    "A literal Garden": 0,
    "Ice Cream": 0,
    "Cake": 0,
    "Pie": 0,
    "Coffee": 0,
    "Tea": 0,
    "Unicorn Tears": 0
    }

items()        
        
        
        
        
        
    
    