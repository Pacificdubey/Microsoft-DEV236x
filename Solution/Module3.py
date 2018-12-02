//maximum order value
max_order = 100

//minimum order value
min_order = .25

//price of each value
price = 7.99

//take input from user
order_amount = input("Enter cheese order weight(numerical valure):")

//changing string to float
order_amount = float(order_amount)

if order_amount>max_order:
    print(order_amount,"is more than currently available stock")
elif  order_amount<min_order:
    print(order_amount,"is below minimum order amount")
else:
    print(order_amount,"costs$",order_amount*price)
