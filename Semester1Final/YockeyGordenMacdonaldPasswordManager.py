from ClassPasswordChecker import PasswordChecker
from PasswordGenerator import PasswordGenerator



password=input("Please enter the master password then if you don't know a password then type 'create' ")
if password!="create":      #if the user has their own password it will go through the password checker and if it doesn't meet the requirements then it will ask for a password again or they have the option of doing a random password
    while password!="create":
        pc=PasswordChecker(password)
        if "False" in str(pc):
            print("That password does not meet the requirements")
            password=input("Please enter the password then if you don't know a password then type 'create' ")
        else:       #if the password meets the requirements then it will append it to the list
            password=password
            break
userName=input("Enter your username ")
passWordUI=input("Enter the password ")
passwordTries=0
            #[[what it's for][username][password]]
homePasswords=[[],[],[]]
workPasswords=[[],[],[]]
entertainmentPasswords=[[],[],[]]
billsPasswords=[[],[],[]]
randomPasswords=[[],[],[]]
masterPasswords=[homePasswords,workPasswords,entertainmentPasswords,billsPasswords,randomPasswords]
#bander said to have 3 lists inside the home, work, etc ones. Example: homePasswords=[[what the password is for],[usernames],[passwords]]

#make the password generator a function     possibly a class but ask bander 

#make the password checker a class too 



PasswordChecker(password)               #this is the password checker as a class 




while passwordTries!=5:     #will let the user enter the password 5 times. if they don't get it in 5 the file will stop. If they enter the right password it will start the program
    if passWordUI!=password:
        passwordTries+=1
        passWordUI=input("Enter the password ")
    else:       #if password is right then it will start the program
        ui=input("What kind of password do you want to store: home, work, entertainment, bills, or random. If you are done type 'done'. If you would like to print out your passwords type 'print'. If you would like to edit type 'edit' ").lower()
        while ui!="done":       #this keeps the program running until the user types done
            if ui==("home"):        #if the user wants to put passwords in the home section it will ask for what the password is for, the username,and the password and append that all to the home list
                reason=input("What is this password for? ")
                homePasswords[0].append(reason)
                username=input("What is the user name for it? ")
                homePasswords[1].append(username)
                password=input("Please enter the password then if you don't know a password then type 'create' ")
                if password!="create":      #if the user has their own password it will go through the password checker and if it doesn't meet the requirements then it will ask for a password again or they have the option of doing a random password
                    while password!="create":
                        pc=PasswordChecker(password)
                        if "False" in str(pc):
                            print("That password does not meet the requirements")
                            password=input("Please enter the password then if you don't know a password then type 'create' ")
                        else:               #if the password meets the requirements then it will append it to the list
                            homePasswords[2].append(password)
                            print(homePasswords)
                            break
                else:       #if the user puts create then it will call the password generator class and append the random password to the list
                    pg=PasswordGenerator()
                    homePasswords[2].append(pg.__str__())
                    print(homePasswords)
                #it will then ask where they want to store another password to keep the program running until they say done
                ui=input("What kind of password do you want to store: home, work, entertainment, bills, or random. If you are done type 'done'.If you would like to print out your passwords type 'print'. If you would like to edit type 'edit' ").lower()
            elif ui=="work":            #if the user wants to put passwords in the work section it will ask for what the password is for, the username,and the password and append that all to the work list
                reason=input("What is this password for? ")
                workPasswords[0].append(reason)
                username=input("What is the user name for it? ")
                workPasswords[1].append(username)
                password=input("Please enter the password then if you don't know a password then type 'create' ")
                if password!="create":      #if the user has their own password it will go through the password checker and if it doesn't meet the requirements then it will ask for a password again or they have the option of doing a random password
                    while password!="create":
                        pc=PasswordChecker(password)
                        if "False" in str(pc):
                            print("That password does not meet the requirements")
                            password=input("Please enter the password then if you don't know a password then type 'create' ")
                        else:       #if the password meets the requirements then it will append it to the list
                            workPasswords[2].append(password)
                            print(workPasswords)
                            break
                else:       #if the user puts create then it will call the password generator class and append the random password to the list
                    pg=PasswordGenerator()
                    workPasswords[2].append(pg.__str__())
                    print(workPasswords)
                ui=input("What kind of password do you want to store: home, work, entertainment, bills, or random. If you are done type 'done'. If you would like to print out your passwords type 'print'. If you would like to edit type 'edit'  ").lower()
            elif ui=="entertainment":       #if the user wants to put passwords in the entertainment section it will ask for what the password is for, the username,and the password and append that all to the entertainment list
                reason=input("What is this password for? ")
                entertainmentPasswords[0].append(reason)
                username=input("What is the user name for it? ")
                entertainmentPasswords[1].append(username)
                password=input("Please enter the password then if you don't know a password then type 'create' ")
                if password!="create":      #if the user has their own password it will go through the password checker and if it doesn't meet the requirements then it will ask for a password again or they have the option of doing a random password
                    while password!="create":
                        pc=PasswordChecker(password)
                        if "False" in str(pc):
                            print("That password does not meet the requirements")
                            password=input("Please enter the password then if you don't know a password then type 'create' ")
                        else:       #if the password meets the requirements then it will append it to the list
                            entertainmentPasswords[2].append(password)
                            print(entertainmentPasswords)
                            break
                else:       #if the user puts create then it will call the password generator class and append the random password to the list
                    pg=PasswordGenerator()
                    entertainmentPasswords[2].append(pg.__str__())
                    print(entertainmentPasswords)
                ui=input("What kind of password do you want to store: home, work, entertainment, bills, or random. If you are done type 'done' If you would like to print out your passwords type 'print'. If you would like to edit type 'edit' ").lower()
            elif ui=="bills":               #if the user wants to put passwords in the bills section it will ask for what the password is for, the username,and the password and append that all to the bills list
                reason=input("What is this password for? ")
                billsPasswords[0].append(reason)
                username=input("What is the user name for it? ")
                billsPasswords[1].append(username)
                password=input("Please enter the password then if you don't know a password then type 'create' ")
                if password!="create":      #if the user has their own password it will go through the password checker and if it doesn't meet the requirements then it will ask for a password again or they have the option of doing a random password
                    while password!="create":
                        pc=PasswordChecker(password)
                        if "False" in str(pc):
                            print("That password does not meet the requirements")
                            password=input("Please enter the password then if you don't know a password then type 'create' ")
                        else:       #if the password meets the requirements then it will append it to the list
                            billsPasswords[2].append(password)
                            print(billsPasswords)
                            break
                else:       #if the user puts create then it will call the password generator class and append the random password to the list
                    pg=PasswordGenerator()
                    billsPasswords[2].append(pg.__str__())
                    print(billsPasswords)
                ui=input("What kind of password do you want to store: home, work, entertainment, bills, or random. If you are done type 'done'. If you would like to print out your passwords type 'print'. If you would like to edit type 'edit' ").lower()
            elif ui=="random":              #if the user wants to put passwords in the random section it will ask for what the password is for, the username,and the password and append that all to the random list
                reason=input("What is this password for? ")
                randomPasswords[0].append(reason)
                username=input("What is the user name for it? ")
                randomPasswords[1].append(username)
                password=input("Please enter the password then if you don't know a password then type 'create' ")
                if password!="create":      #if the user has their own password it will go through the password checker and if it doesn't meet the requirements then it will ask for a password again or they have the option of doing a random password
                     while password!="create":
                        pc=PasswordChecker(password)
                        if "False" in str(pc):
                            print("That password does not meet the requirements")
                            password=input("Please enter the password then if you don't know a password then type 'create' ")
                        else:       #if the password meets the requirements then it will append it to the list
                            randomPasswords[2].append(password)
                            print(randomPasswords)
                            break
                else:       #if the user puts create then it will call the password generator class and append the random password to the list
                    pg=PasswordGenerator()
                    randomPasswords[2].append(pg.__str__())
                    print(randomPasswords)
                ui=input("What kind of password do you want to store: home, work, entertainment, bills, or random. If you are done type 'done'. If you would like to print out your passwords type 'print'. If you would like to edit type 'edit' ").lower()
            elif ui=="print":
                print("\t Username:",userName)
                print("\t Home Passwords:")
                print("For What:\t Username:\t Password:")
                for i in range(len(homePasswords[0])):      #this will grab the length of the first list in the home passwords list and see how many there are 
                    for j in range (len(homePasswords)):    #this will grab 3 because there is 3 lists in each one
                        print(homePasswords[j][i],end="\t\t") #this will print the first item in every list and then print a new line and go through this cycle for as many items are in the list
                    print()
                print("\t Work Passwords:")
                for i in range(len(workPasswords[0])):      #this will grab the length of the first list in the home passwords list and see how many there are 
                    for j in range (len(workPasswords)):    #this will grab 3 because there is 3 lists in each one
                        print(workPasswords[j][i],end="\t\t") #this will print the first item in every list and then print a new line and go through this cycle for as many items are in the list
                    print()
                print("\t Entertainment Passwords:")
                for i in range(len(entertainmentPasswords[0])):      #this will grab the length of the first list in the home passwords list and see how many there are 
                    for j in range (len(entertainmentPasswords)):    #this will grab 3 because there is 3 lists in each one
                        print(entertainmentPasswords[j][i],end="\t\t") #this will print the first item in every list and then print a new line and go through this cycle for as many items are in the list
                    print()
                print("\t Bills Passwords:")
                for i in range(len(billsPasswords[0])):      #this will grab the length of the first list in the home passwords list and see how many there are 
                    for j in range (len(billsPasswords)):    #this will grab 3 because there is 3 lists in each one
                        print(billsPasswords[j][i],end="\t\t") #this will print the first item in every list and then print a new line and go through this cycle for as many items are in the list
                    print()
                print("\t Random Passwords:")
                for i in range(len(randomPasswords[0])):      #this will grab the length of the first list in the home passwords list and see how many there are 
                    for j in range (len(randomPasswords)):    #this will grab 3 because there is 3 lists in each one
                        print(randomPasswords[j][i],end="\t\t") #this will print the first item in every list and then print a new line and go through this cycle for as many items are in the list
                    print()
                ui=input("What kind of password do you want to store: home, work, entertainment, bills, or random. If you are done type 'done'. If you would like to print out your passwords type 'print'. If you would like to edit type 'edit' ").lower()
            elif ui=="edit":
                editUI=input("What is the password for that you would like to change? ")
                if editUI in homePasswords[0]:
                    ind=homePasswords[0].index(editUI)
                    print(ind)
                    newPass=input("What would you like to change the password to...If you want another random one type 'create' ")
                    if newPass!="create":      #if the user has their own password it will go through the password checker and if it doesn't meet the requirements then it will ask for a password again or they have the option of doing a random password
                        while newPass!="create":
                            pc=PasswordChecker(newPass)
                            if "False" in str(pc):
                                print("That password does not meet the requirements")
                                newPass=input("Please enter the password then if you don't know a password then type 'create' ")
                            else:       #if the password meets the requirements then it will append it to the list
                                homePasswords[2][ind]=newPass
                                print(randomPasswords)
                                break
                    else:       #if the user puts create then it will call the password generator class and append the random password to the list
                        pg=PasswordGenerator()
                        homePasswords[2][ind]=(pg.__str__())
                        print(homePasswords)            #IT IS NOT TRIGERING THIS WHEN THE FIRST PASSWORD DOESN'T MEET REQ. FIX THIS
                        ui=input("What kind of password do you want to store: home, work, entertainment, bills, or random. If you are done type 'done'. If you would like to print out your passwords type 'print'. If you would like to edit type 'edit' ").lower()
                
                                



                    #homePasswords[2][ind]=newPass 
                    #print(homePasswords[2][ind])
                    #print(homePasswords)
                



            else:       #if they didn't type in one of the categories then it will tell them that and ask again
                print("That wasn't one of the choices")
                ui=input("What kind of password do you want to store: home, work, entertainment, bills, or random. If you are done type 'done'. If you would like to print out your passwords type 'print'. If you would like to edit type 'edit' ").lower()
        
        if ui=="done":          #if the user is done it will break the loop and set the passwordTries to 5 which will break the first while loop and end the whole program
            passwordTries=5        



