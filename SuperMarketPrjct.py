from datetime import datetime

# Items available in Supermarket

name = input("Enter your Name:")
list_items = '''
Rice     Rs.50/kg
Dal      Rs.80/kg
Oil      Rs.100/kg
Sugar    Rs.50/kg
Salt     Rs.22/kg
Coffee   Rs.90/kg
Tea      Rs.150/kg
Paneer   Rs.400/kg

'''
print(list_items)

# Declaration 

price = 0
total_price = 0
final_price = 0
pricelist = []
items_list = []
quantity_list = []
price_list = []

# Rates for items

items_dict = {
     'Rice':50,
     'Dal':80,
     'Oil':100,
     'Sugar':50,
     'Salt':22,
     'Coffee':90,
     'Tea':150,
     'Paneer':400

}
option = int(input("For List of items Press 1: "))
if option == 1:
    print(list_items)
    for i in range(len(items_dict)):
        input_1 = int(input("If you want to buy press 1 or press 2 for exit:"))
        if input_1 == 2:
            break
        if input_1 == 1:
            item = input("Enter your item name:")
            quantity = int(input("Required quantity:"))
            if item in items_dict.keys():
                price = quantity * (items_dict[item])
                pricelist.append((item,quantity,items_dict,price))
                total_price += price
                items_list.append(item)
                quantity_list.append(quantity)
                price_list.append(price)
                gst = (total_price * 5)/100
                final_price = gst + total_price
            else:
                print("Selected item is Unavailable,Sorry!")
else:
    print("You entered wrong number")

final_input = input("Can I bill the items?Yes or No:")
if final_input == "Yes":
    pass
    if final_price != 0:
        print(25 * "*","Super Market",30 * "*")
        print(28 * " ","Ongole")
        print("Name:",name,30 * " ","Date:",datetime.now())
        print(75 * "-")
        print("S.No",8 * " ","Items",8 * " ","Quantity",3 * " ","price")
        print(75 * "-")
        for i in range(len(pricelist)):
            print(i,12 * " ",items_list[i],10 * " ",quantity_list[i],5 * " ",price_list[i])
        print(75 * "-")
        print(50 * " ","Total Amount:","Rs.",total_price)
        print("Gst Amount",50 * " ","Rs.",gst)
        print(75 * "-")
        print(50 * " ",'Final Amount:','Rs.',final_price)
        print(75 * "-")
        print(50 * " ","Thanks for Visiting")
        print(75 * "-")

    
