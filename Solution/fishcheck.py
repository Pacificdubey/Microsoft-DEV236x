//fish function with two parameters
def fishstore(fish,price):
    return("Fish Type:"+ " " +fish + " " +"costs"+" "+"$"+price)
    
 //Input from user for fish name   
def fish_entry():
    fish_entry = input("Enter the fish name:")
    return fish_entry
    
 //get fish price from user
def get_price():
    fish_price = input("Enter the fish price(no symbols):")
    return fish_price
    
   //print these values
print(fishstore(fish_entry(),get_price()))
