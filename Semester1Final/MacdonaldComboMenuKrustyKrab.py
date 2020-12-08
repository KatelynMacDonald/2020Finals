def tax(subtotal):
    theTotalAmount=subtotal*(0.07)
    return theTotalAmount
from InputCheck import YNInputCheck 
from InputCheck import SMLInputCheck



print("""
        Menu
Krabby Patty...........1.25         Krabby Meal...........3.50
    w/sea cheese.......1.50         Double Krabby Meal....3.75
Double Krabby Patty....2.00         Triple Krabby Meal....4.00
    w/sea cheese.......2.25         Salty Sea Dog.........1.25
Triple Krabby Patty....3.00         Footlong..............2.00
    w/sea cheese.......3.25         Sailors Surprise......3.00
                                    Golden Loaf...........2.00 
Coral Bits                              w/sauce...........2.50
    Small..............1.00
    Medium.............1.25         Kelp Shake............2.00
    Large..............1.50
                                    Seafoam Soda
Kelp Rings.............1.50             Small.............1.00
    salty sauce........0.50             Medium............1.25
                                        Large.............1.50
""")

mainOrder=[]

subtotal=0
finalAmount=0

def orderFunction(ui):
    order=[]
    subtotal=0
    while ui!="next":      #while the user input doesn't = next it will add the amount of money that the user choose and append what food they want to the order list
        if ui=="krabby patty":
                subtotal+=1.25
                yN=True
                ui=input("Would you like sea cheese on it? y or n ").lower()
                while (yN):
                    IC=YNInputCheck(ui)
                    #if "False" in str(IC):
                        
                    if "False" in str(IC):
                        break
                if "y" in str(IC):
                    subtotal+=0.25
                    order.append("krabby patty w/ sea cheese")
                elif "n" in str(IC):
                    order.append("krabby patty")
        elif ui=="double krabby patty":
            subtotal+=2.00
            yN=True
            ui=input("Would you like sea cheese on it? y or n ").lower()
            while (yN):
                    IC=YNInputCheck(ui)
                    #if "False" in str(IC):
                        
                    if "False" in str(IC):
                        break
            if "y" in str(IC):
                subtotal+=0.25
                order.append("double krabby patty w/ sea cheese")
            elif "n" in str(IC):
                order.append("double krabby patty")
        elif ui=="triple krabby patty":
            subtotal+=3.00
            yN=True
            ui=input("Would you like sea cheese on it? y or n ").lower()
            while (yN):
                    IC=YNInputCheck(ui)
                    #if "False" in str(IC):
                        
                    if "False" in str(IC):
                        break
            if "y" in str(IC):
                subtotal+=0.25
                order.append("triple krabby patty w/ sea cheese")
            elif "n" in str(IC):
                order.append("triple krabby patty")
        
        elif ui=="coral bits":
            subtotal+=1.00
            sML=True
            ui=(input("What size would you like s,m,l? ")).lower()
            while (sML):
                SC=SMLInputCheck(ui)
                if "Done" in str(SC):
                    break
            if "s" in str(SC):
                order.append("small seafoam soda")
            elif "m" in str(SC):
                subtotal+=0.25
                order.append("medium coral bits")
            elif "l" in str(SC):
                subtotal+=0.50
                order.append("large coral bits")

            
        elif ui=="kelp rings":
            subtotal+=1.50
            yN=True
            ui=input("Would you like salty sauce? y or n ").lower()
            while (yN):
                    IC=YNInputCheck(ui)
                    #if "False" in str(IC):
                        
                    if "False" in str(IC):
                        break
            if "y" in str(IC):
                subtotal+=0.50
                order.append("kelp rings w/ salty sauce")
            elif "n" in str(IC):
                order.append("kelp rings")
        elif ui=="krabby meal":
            subtotal+=3.50
            order.append(ui)
        elif ui=="double krabby meal":
            subtotal+=3.75
            order.append(ui)
        elif ui=="triple krabby meal":
            subtotal+=4.00
            order.append(ui)
        elif ui=="salty sea dog":
            subtotal+=1.25
            order.append(ui)
        elif ui=="footlong":
            subtotal+=2.00
            order.append(ui)
        elif ui=="sailors surprise":
            subtotal+=3.00
            order.append(ui)
        elif ui=="golden loaf":
            subtotal+=2.00
            yN=True
            ui=input("Would you like it with sauce? y or n ").lower()
            while (yN):
                    IC=YNInputCheck(ui)
                    #if "False" in str(IC):
                        
                    if "False" in str(IC):
                        break
            if "y" in str(IC):
                subtotal+=0.50
                order.append("golden loaf w/ sauce")
            else:
                order.append("golden loaf")
        elif ui=="kelp shake":
            subtotal+=2.00
            order.append(ui)
        elif ui=="seafoam soda":
            subtotal+=1.00
            sML=True
            ui=input("What size would you like s,m,l? ").lower()
            while (sML):
                SC=SMLInputCheck(ui)
                if "Done" in str(SC):
                    break
            if "s" in str(SC):
                order.append("small seafoam soda")
            elif "m" in str(SC):
                subtotal+=0.25
                order.append("medium seafoam soda")
            elif "l" in str(SC):
                subtotal+=0.50
                order.append("large seafoam soda")
        elif ui=="change":
            
            print((str(', '.join(order))))
            ui=input("What would you like to take out(if you don't want to take anything out type'n') ").lower()
            while ui!="n":          #this keeps looping until the user doesn't want to take anything else out
                if ui in order:
                    order.remove(ui)        #this will remove the food item from the list
                    print((str(', '.join(order))))
                    #all of these will look at what the user wanted out and subtract it from the total
                    #MAKE THIS ALL INTO 2 LISTS AND PULL EACH INDEX LIKE IN PASSWORD MANAGER
                    food=["krabby patty","krabby patty w/ sea cheese","double krabby patty","double krabby patty w/ sea cheese","triple krabby patty","triple krabby patty w/ sea cheese","small coral bits","medium coral bits","large coral bits","kelp rings","kelp rings w/ salty sauce", "krabby meal","double krabby meal","triple krabby meal","salty sea dog","footlong","sailors surprise","golden loaf","golden loaf w/ sauce","kelp shake","medium seafoam soda","large seafoam soda","small seafoam soda"]
                    price=[1.25,1.50,2.00,2.25,3.00,3.25,1.00,1.25,1.50,1.50,2.00,3.50,3.75,4.00,1.25,2.00,3.00,2.00,2.50,2.00,1.25,1.50,1.00]
                    ind=food.index(ui)
                    subtotal-=price[ind]
                    print (subtotal)
                    """if ui=="krabby patty":
                        subtotal-=1.25
                    elif ui=="krabby patty w/ sea cheese":
                        subtotal-=1.50
                    elif ui=="double krabby patty":
                        subtotal-=2.00
                    elif ui=="double krabby patty w/ sea cheese":
                        subtotal-=2.25
                    elif ui=="triple krabby patty":
                        subtotal-=3.00
                    elif ui=="triple krabby patty w/ sea cheese":
                        subtotal-=3.25
                    elif ui=="small coral bits":
                        subtotal-=1.00
                    elif ui=="medium coral bits":
                        subtotal-=1.25
                    elif ui=="large coral bits":
                        subtotal-=1.50
                    elif ui=="kelp rings":
                        subtotal-=1.50
                    elif ui=="kelp rings w/ salty sauce":
                        subtotal-=2.00
                    elif ui=="krabby meal":
                        subtotal-=3.50
                    elif ui=="double krabby meal":
                        subtotal-=3.75
                    elif ui=="triple krabby meal":
                        subtotal-=4.00
                    elif ui=="salty sea dog":
                        subtotal-=1.25
                    elif ui=="footlong":
                        subtotal-=2.00
                    elif ui=="sailors surprise":
                        subtotal-=3.00
                    elif ui=="golden loaf":
                        subtotal-=2.00
                    elif ui=="golden loaf w/ sauce":
                        subtotal-=2.50
                    elif ui=="kelp shake":
                        subtotal-=2.00
                    elif ui=="medium seafoam soda":
                        subtotal-=1.25
                    elif ui=="large seafoam soda":
                        subtotal-=1.50
                    elif ui=="small seafoam soda":
                        subtotal-=1.00"""

                    ui=input("What would you like to take out(if you don't want to take anything out type'n') ").lower()

                else:   #this makes sure it is actually in the list
                    print("That is not in your order...")
                    ui=input("What would you like to take out(if you don't want to take anything out type'n') ").lower()
        else:
            print("That is not an option")


                
            

        ui=input("What would you like on this order(if you are done type 'next')(if you would like to change your order type'change') REMEMBER: You can only edit your meal while you are inside the order ").lower()
        
    #print(subtotal)
    return(order, subtotal)         #if user = next it will return the order list and the subtotal so you can use it later
        


ui=input("What would you like on this order(when you are done on this order type 'next' for a new one)(when you are done ordering type 'done') REMEMBER: You can only edit your meal while you are inside the order   ").lower()

while ui!="done":                               #while the user isn't done with their order
    
    thePersonsOrder=orderFunction(ui)
    mainOrder.append(thePersonsOrder[0])        #this makes what the order of each person is and appends it to the main order
    subtotal+=thePersonsOrder[1]                #takes the subtotal from the function and makes it the subtotal for a global variable so you  can use it later
    ui=input("Would you like to have another order? (when you are done ordering type 'done') REMEMBER: You can only edit your meal while you are inside the order ").lower()


taxAmount=tax(subtotal)

print("Order:")
for i in range(len(mainOrder)):
    print("\tOrder ", i+1 ,":", (str(', '.join(mainOrder[i]))))
print("Subtotal = $", subtotal)
print("Tax = $" , taxAmount)
finalAmount=subtotal+taxAmount
print("Total Amount =$",finalAmount)



"""
for i in range(len(mainOrder)):
    for j in (mainOrder[i]):
        print("Order ", i+1 ,":", j)
"""
"""
for i in range(len(mainOrder)):
    print("Order ", i+1 ,":", (str(', '.join(mainOrder[i]))))"""

#(str(' '.join(lines)))

