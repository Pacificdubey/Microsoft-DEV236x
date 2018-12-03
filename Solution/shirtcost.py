s_price = 6
m_price = 8
l_price = 10
number_s = 0
number_m = 0
number_l = 0
total_shirt =0
while True:
    size = str(input("What is your shirt size?"))
    if size.lower() == 's':
        number_s+=1
    elif size.lower() == 'm':
        number_m+=1
    elif size.lower()=='l':
        number_l+=1
    else:
        print("we do not have it:")
        break
    total_shirt +=1
    cost_s = s_price*number_s 
    cost_m = m_price*number_m
    cost_l = l_price*number_l
    total_cost = s_price*number_s +m_price*number_m + l_price*number_l
    print("Small Shirts costs:",cost_s,"\nMedium Shirts costs:",cost_m,"\nLarge Shirts:",cost_l)
    print("Total shirts",total_shirt,"Total costs:",total_cost)
