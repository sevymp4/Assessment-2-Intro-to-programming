# Assessment 2
import time #Gives a time before codes gets printed
print ("\n\t Vending Machine, Please wait...")
time.sleep(2.2) #Uses the imported time to 
menu = {"A1": {"ItemName": 'Water', "itemPrice": 1.00},
        "A2": {"ItemName": 'Coca cola', "ItemPrice": 2.40},
        "A3": {"ItemName": 'Fanta', "ItemPrice": 2.36},
        "B1": {"ItemName": 'Kitkat',"ItemPrice": 1.95},
        "B2": {"ItemName": 'Lays chips', "ItemPrice": 7.49}, 
        "B3": {"ItemName": 'Vimto',"ItemPrice": 2.00},
        "C1": {"ItemName": 'Oman chips', "ItemPrice": 3.00},
        "C2": {"ItemName": '7 days bread',"ItemPrice": 1.70},
        "C3": {"ItemName": 'Doritos', "ItemPrice": 8.95}
        }

print ('  ======================================')
print ("  ||Welcome to Lanz's Vending Machine!||")
print ('  ======================================')

def menu_items(): #Function to constantly display the menu.

    print("\n\t\t\tHere's our menu")
    print('\n============================================')
    
    for code, details in menu.items():
        
        item_name = details["ItemName"] #Converts the values from ItemName & ItemPrice into a value.
        
        item_price = details.get("ItemPrice") or details.get("itemPrice") 
        
        print(f"Code: {code} | Item: {item_name:12} | Price: ${item_price:.2f}") 

    print('============================================')


balance = 0

def cash_insert(): #Function to insert cash into your balance.
    global balance #The global statement allows for the value to be used in functions without being inside them.
    while True:
        try:
            input_cash = float(input("\nInsert cash (1-100 bills only): "))
        
            if 1 <= input_cash <= 100: #Makes sure that you can only input integers from 1-100 as a substitute from real vending machines that can only take certain bills.
                balance += input_cash
                print(f"\nYour balance is {balance} dhs")
                break
            else:
                print("\nInvalid amount! Please enter cash between 1 and 100.") #If the user were to go above 100 or less than 1.
        except ValueError:
            print("\nInvalid input. Please enter a number.") #If the user inputs a datatype that isn't a string this message is printed. The code then loops back.

def order(): #Function to order items within the menu.
    global balance 
    global price
    global item_name
    print ("\n\t\t\tPlease wait..")
    time.sleep(1)
    print ('\n\t--- Order Process Started ---')
    consumer = input("\nPlease select your item code (Example: A1): ").strip().capitalize() #allows for all inputs to always be capitalized
    if consumer not in menu: #If the user's input is not in the dictionary.
        print ("\nInvalid Item code. Please try again!")
        
        
    
    item_details = menu[consumer]
    item_name = item_details.get("ItemName")
    
    price = item_details.get("ItemPrice") or item_details.get("itemPrice")
    
    while True:
        try:
            insert_cash = input(f"\nYour current balance is {balance}\n\nWould you like to add money?(Y/N): ").strip().capitalize()
            if insert_cash == 'Y':
                cash_insert() #calls the cash_insert function so the user can input a cash amount to their balance
                print ("\nProceeding towards payment..")
                time.sleep(1)
                payment() #Calls the payment function so the user can proceed with the transaction
                break
                
            elif insert_cash == 'N':
                print (f"\nYour current balance is {balance}dhs.")
                print ("\nProceeding towards payment..")
                time.sleep(1)
                payment() #Calls the payment function so the user can proceed with the transaction
                break
            
            else:
                print ("\nThat's not a proper input. \n\nPlease try again") #If the user inputs something aside from y or n it will then loop back.
            
        except ValueError:
            print ("\nThat's not a proper input. \n\nPlease try again") #If the user inputs a datatype that isn't a string this message is printed. The code then loops back.
            
def payment(): #Function to pay for the item.
    global balance
    global price
    global item_name
    
    if balance < price: #calls the function back if user's balance is less than the price
        print ("\nYou don't have enough in your balance please insert cash")
        cash_insert()
        
    pay = input("\nPlease confirm your purchase (Y/N): ").strip().capitalize()
        
    if pay == "Y":
        balance = balance - price
        print (f"\nHere's your {item_name}! \nYour current balance is {balance} dhs")
        continue_shopping()
        
    elif pay == 'N':
        print ("\n\tPayment cancelled.")
        continue_shopping()

def continue_shopping(): #Function to continue shopping
    global balance
    onwards = input("\nWould you like to continue shopping?(Y/N): ").strip().capitalize()
    time.sleep(1)
    
    if onwards == 'Y': #If the user inputs in Y it will then recall the menu function and the ordering function.
        print ("\n\tProceeding back to menu..")
        time.sleep(1)
        menu_items()
        order()
        
    elif onwards == 'N': #If the user inputs in N the code will then print out the code below and stop the code.
        print (f"\nHave a great day! \n\nHere's your {balance} dhs!")
        time.sleep(1)
    
    else:
        print ("\nThat's not a proper input. \n\nPlease try again")
        continue_shopping() #Recalls the function.

menu_items()
order() 