# Sebastian Main

def store_menu():
    print("Welcome to the Python Store!")
    print("These are the items we offer, along with their price:")
    print("	desk $129.90")
    print("	computer $1099")
    print("	lamp $30.50")
    print("	couch $550")
    print("	notebook $20.90")
    
def item_check(user_input, prices):
    for price in prices:
        if user_input == price[0]:
            return True
    return False


def shopping_cart(prices):
    user_input = input("Add to cart: ")
    total = 0
    cart = []
    while user_input != "Done":
        if item_check(user_input, prices) == True:
            for price in prices:
                if user_input == price[0]:
                    total += price[1]
                    cart.append(price[0])
        else:
            print(f"{user_input} isn't listed. Please try again.")
        
       
                    
        user_input = input("Add to cart: ")
        
    print("You have added the follow items to your cart: " + str(cart))
    
    print("Your total is: " + str(total))
                    
                    
    
        

def main():
    desk = ["desk", 129.9]
    computer = ["computer", 1099]
    lamp = ["lamp", 30.5]
    couch = ["couch", 550]
    notebook = ["notebook", 20.9]
    prices = [desk, computer, lamp, couch, notebook]
    store_menu()
    shopping_cart(prices)
    

    # Finish the rest of the code here

main()