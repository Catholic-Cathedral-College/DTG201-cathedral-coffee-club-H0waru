#import
import time


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

def main(): 
    ready = "no"
    while ready != "yes": 
        ready = input("Are you ready to order?: ")
        if ready.lower().strip() == "yes": 