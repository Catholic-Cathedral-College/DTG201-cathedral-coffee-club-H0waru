#import
import time
import ast 
#list for prices
prices = [
    "3.00",
    "3.00",
    "3.50",
    "3.00",
    "4.00",
]

#Menu function
def menu():
    print("*" * 27)
    print("* (1) Flat white    $3.00 *")
    print("* (2) Cappaccino    $3.00 *")
    print("* (3) Latte         $3.50 *")
    print("* (4) Decaf         $3.00 *")
    print("* (5) Hot Chocolate $4.00 *")
    print("*" * 27)


#introduction
def intro():
    print("*-" * 25)
    print("Welcome to CCC Cafe".center(50))
    print("*-" * 25)
    time.sleep(2)
    print("\nPlease have a look at our menu:")
    menu()

#Creating a sugar function 
def sugar():
    sugar = input("Would you like sugar with your order?: ")
    if sugar.lower().format() == "yes": # making sure the code works for uppercase inputs
        print("yes to sugar ")
    elif sugar.lower().format() == "no":
        print("Okay no sugar ")

#running the function of the intro 
intro()
#main start of the program starts here
ready = "no"
while ready != "yes": # creating a loop for orders
    ready = input("Are you ready to order?: ")
    if ready == "no":
        print("Let me know when you are ready to order :)")
    if ready.lower().strip() == "yes":
        name = input("order name: ")
        break
order = int(input("\nWhat would you like to order? \n(please input the number beside the coffee you would like to order):"
            ))
#outcomes of each coffee

if order == 1:
    print("A flat white")
    quantity = int(input("How many flat white's do you want?:"))
    print("{} flat whites ".format(quantity))
    sugar()
    #Creating a payment method
    total = quantity * float(prices[0])
    print("Your total order comes to ${}".format(total))
    payment = input("How would you like to pay for your order? Card or Cash: ")
    if payment.lower().strip() == "card": #creating payment method for card
        print("Please swipe you card or use paywave")
        time.sleep(1)
        print("Processing payment...")
        time.sleep(2)
        print("Accepted")
    elif payment.strip().lower() == "cash": # creating payment method for cash 
        cash = int(
            input(
                "Please input the amount of cash you would like to pay with$: ")
        )
        total_order = total - cash
        total_order = abs(total_order) # making sure that the value of total_order is given back 
        if cash >= total:
            print("Here is your change ${}".format(total_order)) # giving customer there change 
        elif cash < total:
            print("You do not have enough money")
            exit()
#Seperation 2
if order == 2:
    print("A Cappaccino")
    quantity = int(input("How many cappaccino's do you want?:"))
    print("{} cappaccino's ".format(quantity))
    sugar()
    #Creating a payment method
    total = quantity * float(prices[0])
    print("Your total order comes to ${}".format(total))
    payment = input("How would you like to pay for your order? Card or Cash: ")
    if payment.lower().strip() == "card":
        print("Please swipe you card or use paywave")
        time.sleep(1)
        print("Processing payment...")
        time.sleep(2)
        print("Accepted")
    elif payment.strip().lower() == "cash":
        cash = int(
            input(
                "Please input the amount of cash you would like to pay with: ")
        )
        total_order = total - cash
        total_order = abs(total_order)
        if cash >= total:
            print("Here is your change ${}".format(total_order))
        elif cash < total:
            print("You do not have enough money")
            exit()
#seperation for 3
if order == 3:
    print("A Latte")
    quantity = int(input("How many Latte's do you want?:"))
    print("{} Latte ".format(quantity))
    sugar()
    #Creating a payment method
    total = quantity * float(prices[0])
    print("Your total order comes to ${}".format(total))
    payment = input("How would you like to pay for your order? Card or Cash: ")
    if payment.lower().strip() == "card":
        print("Please swipe you card or use paywave")
        time.sleep(1)
        print("Processing payment...")
        time.sleep(2)
        print("Accepted")
    elif payment.strip().lower() == "cash":
        cash = int(
            input(
                "Please input the amount of cash you would like to pay with: ")
        )
        total_order = total - cash
        total_order = abs(total_order)
        if cash >= total:
            print("Here is your change ${}".format(total_order))
        elif cash < total:
            print("You do not have enough money")
            exit()
# seperation for 4 
if order == 4:
    print("A decaf")
    quantity = int(input("How many decaf's do you want?:"))
    print("{} decaf ".format(quantity))
    sugar()
    #Creating a payment method
    total = quantity * float(prices[0])
    print("Your total order comes to ${}".format(total))
    payment = input("How would you like to pay for your order? Card or Cash: ")
    if payment.lower().strip() == "card":
        print("Please swipe you card or use paywave")
        time.sleep(1)
        print("Processing payment...")
        time.sleep(2)
        print("Accepted")
    elif payment.strip().lower() == "cash":
        cash = int(
            input(
                "Please input the amount of cash you would like to pay with: ")
        )
        total_order = total - cash
        total_order = abs(total_order)
        if cash >= total:
            print("Here is your change ${}".format(total_order))
        elif cash < total:
            print("You do not have enough money")
            exit()
#seperation for 5
if order == 5:
    print("A hot chocolate")
    quantity = int(input("How many hot chocolate's do you want?:"))
    print("{} hot chocolate's ".format(quantity))
    sugar()
    #Creating a payment method
    total = quantity * float(prices[0])
    print("Your total order comes to ${}".format(total))
    payment = input("How would you like to pay for your order? Card or Cash: ")
    if payment.lower().strip() == "card":
        print("Please swipe you card or use paywave")
        time.sleep(1)
        print("Processing payment...")
        time.sleep(2)
        print("Accepted")
    elif payment.strip().lower() == "cash": # allowing for uppercase input 
        cash = int(
            input(
                "Please input the amount of cash you would like to pay with: ")
        )
        total_order = total - cash
        total_order = abs(total_order)
        if cash >= total:
            print("Here is your change ${}".format(total_order))
        elif cash < total:
            print("You do not have enough money")
            exit()

#reciept function 
def reciept():
    print("\n")
    print("-" * 30)
    print("Reciept for {}\n".format(name))
    print("order: {}".format(order))
    print("quantity:{}\n".format(quantity))
    print("{} your total order is ${}\n".format(name, total))
    print("Payment method was {}".format(payment))
    if payment == "cash":
        print("Change: {}".format(total_order))
    print("-" * 30)

#calling for function 
reciept()
#printing ending
print("Thank you for ordering at CCC cafe enjoy the rest of your day! :)")