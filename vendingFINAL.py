snackTotal = 0
drinkTotal = 0

def printMenu(): #prints menu
    print("\033[1;33;40m===============| M E N U |===============\033[0m\n\t")
    print("\t\033[1;36;40m [1] D R I N K S\033[0m\t\n")
    print("\t\033[1;36;40m [2] S N A C K S\033[0m\t\n")  
        
def printDrinks():#prints drinks menu
    
    drinkTotal = 0 #default value at start
    
    print("\033[1m==========| D R I N K S |==========\033[0m\n")  
    print("\t1. Coca Cola (2.00) \n\t2. Sprite (2.00) \n\t3. Mountain Dew (2.50) \n\t4. Arwa Water (1.00) \n\t5. Return\n")
    while True:
        
        answer = input("Select a drink: ") #asks for the user to select a number
        
        if answer == "1":
            print("Coca Cola (2.00) has been added.")
            drinkTotal = drinkTotal + 2.00
        elif answer == "2":
            print("Sprite (2.00) has been added.")
            drinkTotal = drinkTotal + 2.00
        elif answer == "3":
            drinkTotal = drinkTotal + 2.50
            print("Mountain Dew (2.50) has been added.")
        elif answer == "4":
            print("Arwa Water (1.00) has been added.")
            drinkTotal = drinkTotal + 1.00
        elif answer == "5":
            print("Your current total due is", drinkTotal)
            break
        else:
            print("Invalid input")
    return drinkTotal #returns the value of the drinkTotal

def printSnacks():#prints snacks
    
    snackTotal = 0 #default value at start
    
    print("\n\033[1m==========| S N A C K S |==========\033[0m\n") 
    print("\t1. KitKat (2.00) \n\t2. Oreos (2.00) \n\t3. Lays (2.50) \n\t4. Cheetos (2.50)\n\t5. Return\n")
        
    while True:
        
        answer = input("Select a snack: ") #asks for the user to select a number
        
        if answer == "1":
            print("KitKat (2.00) has been added.")
            snackTotal = snackTotal + 2.00
        elif answer == "2":
            print("Oreos (2.00) has been added.")
            snackTotal = snackTotal + 2.00
        elif answer == "3":
            snackTotal = snackTotal + 2.50
            print("Lays (2.50) has been added.")
        elif answer == "4":
            print("Cheetos (2.50) has been added.")
            snackTotal = snackTotal + 2.50
        elif answer == "5":
            print("Your current total due is", snackTotal)
            break 
        else:
            print("Invalid input")
            
    return snackTotal #returns the value of snackTotal

def printPay(snackTotal, drinkTotal):
    
    amount = snackTotal + drinkTotal #combines the total of the drinks and snacks chosen by the user
    print("Your total amount is", amount)
    
    while True:
         cash = float(input("Enter your cash: ")) #allows the user to enter cash
         print("You have given", cash)
         change = cash - amount #subtracts the cash used to the total amount of the items
         
         if cash < amount: #if cash provided by user is less than the total amount of the items
                print("Insufficient funds.")
         else:
                print("Your change is", change) #prints the change
                print("Thank you for choosing to use my vending machine!")
                break

#main program
amount = 0

printMenu() #prints the menu 

while True:
    
        choice = input("Press '\033[1m1\033[0m' to check our available drinks.\nPress '\033[1m2\033[0m' to check our available snacks.\nPress '\033[1m3\033[0m' to pay.\n\033[1mENTER THE NUMBER:\033[0m ") 

        if choice == "1":
            drinkTotal = printDrinks() #prints the drink menu
        elif choice == "2":
            snackTotal = printSnacks() #prints the snack menu
        elif choice == "3":
            printPay(snackTotal, drinkTotal)
            break
        else:
            print("Invalid input.")
            
        
            
            


    

      
            
        




