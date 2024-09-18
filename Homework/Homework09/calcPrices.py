# Sebastian Main

def main():
    prices = get_prices()
    quantity = get_quantity()
    calc_price(prices, quantity)
        
def get_prices():
    f = open("shoppingCart.txt")
    prices = {}
    lines = f.readlines()
    for line in lines:
        line = line.split(",")
        item = line[1]
        item_list = float(item)
        prices[line[0]] = item_list
    print("---prices dictionary---")
    print(prices)
    f.close()
    return prices
    
def get_quantity():
    f = open("shoppingCart.txt")
    quantity = {}
    lines = f.readlines()
    for line in lines:
        line = line.split(",")
        amount = line[2]
        amount_list = int(amount.strip())
        quantity[line[0]] = amount_list
    print("---quantity dictionary---")
    print(quantity)
    f.close()
    return quantity
    
def calc_price(prices, quantity):
    f2= open("prices.txt", "w")
    for item in prices:
        price = prices[item]
        stock = quantity[item]
        stock_price = price * stock
        f2.write(f"{item},{stock_price}\n")
    
    total_cost = 0
    f = open("shoppingCart.txt")
    lines = f.readlines()
    for line in lines:
        line = line.split(",")
        cost = float(line[1]) * float(line[2])
        total_cost += cost
    f2.write("total," + str(total_cost))
    f.close()


main()