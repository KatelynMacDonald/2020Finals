class YNInputCheck:
    def __init__(self,ui):          #this is to check for if the user put in a y or n
        self.userInput=ui
        self.yN=True
        while (self.yN):            
                    if self.userInput=="y" or self.userInput=="n":  #if they put in y or n it will make self.yN false
                        self.yN=False
                    else:
                        self.yN=True        #if they don't it will keep asking the question until they do
                        self.userInput=input("You need to type in y or n ")
                        
    def __str__(self):
        if self.yN==False:      #this will return false or true and if they said yes or no
            return str("False"+self.userInput)
        elif self.yN==True:
            return str("True"+self.userInput)



class SMLInputCheck:            #this is to check to see if they put in s, m, or l
    def __init__(self,ui):
        self.userInput=ui
        self.SML=True
        while (self.SML):       #if they do put it s, m, or l it will break the while loop
            if self.userInput=="s" or self.userInput=="m" or self.userInput=="l":
                self.SML=False
            else:
                self.SML=True           #if they don't it will keep asking the question until they put in one of the three
                self.userInput=input("You need to type in s, m, or l ")

    def __str__(self):
        if self.SML==False:             #this returns done and if they said s, m, or l
            return str("Done"+self.userInput)
        elif self.SML==True:
            return str("True"+self.userInput)