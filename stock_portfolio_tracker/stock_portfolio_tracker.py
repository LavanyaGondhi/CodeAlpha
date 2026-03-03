stock={'ALSA':150,'RVR':200,'SLR':300,'ULR':400}
stock_n=input("Enter a stock name:")
stock_name=stock_n.upper()
quantity=int(input("Enter the quantity required:"))
if stock_name in stock:
    price=stock[stock_name]
    total_price=price*quantity
    print("Stock:",stock_name)  
    print("Price per stock:",price) 
    print("Quantity:",quantity) 
    print("Total Price:",total_price)
else:
    print("Stock not available")