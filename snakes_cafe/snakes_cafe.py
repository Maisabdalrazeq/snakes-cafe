
  
welcoming_msg = """
**************************************
**    Welcome to the Snakes Cafe!   **
**    Please see our menu below.    **
**
** To quit at any time, type "quit" **
**************************************
"""
print(welcoming_msg)

menu= """
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

Drinks
------
Coffee
Tea
Unicorn Tears

***********************************
** What would you like to order? **
***********************************
"""

print(menu)

foodList = ["Wings","Cookies","Spring Rolls","Salmon","Steak","Meat Tornado","A Literal Garden","Ice Cream","Cake","Pie","Coffee","Tea","Unicorn Tears"]
userOrdersList = []
userInput = True

while userInput:
        
    if len(userOrdersList):
        print('      **********************************      ')
       
      
        print('If you have anothr order type it or type quit to exit ???')
       
    userOrder = str(input()).capitalize()

    if userOrder in foodList:
        userOrdersList.append(userOrder)
        
        x = userOrdersList.count(userOrder)
            
        print(f"*** {x} order of {userOrder} have been added to your meal ***")



    elif userOrder == 'Quit':
        break

    else:
        print('Sorry we did not have your order in our menu ..try again ! ') 
