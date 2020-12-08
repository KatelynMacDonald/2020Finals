class YNInputCheck:
    def __init__(self,ui):
        self.userInput=ui
        self.yN=True
        while (self.yN):
                    if self.userInput=="y" or self.userInput=="n":
                        self.yN=False
                    else:
                        self.yN=True
                        self.userInput=input("You need to type in y or n ")
                        
    def __str__(self):
        print(self.yN)
        if self.yN==False:
            return str("False"+self.userInput)
        elif self.yN==True:
            return str("True"+self.userInput)



class SMLInputCheck:
    def __init__(self,ui):
        self.userInput=ui
        self.SML=True
        while (self.SML):
            if self.userInput=="s" or self.userInput=="m" or self.userInput=="l":
                self.SML=False
            else:
                self.SML=True
                self.userInput=input("You need to type in s, m, or l ")

    def __str__(self):
        print(self.SML)
        if self.SML==False:
            return str("Done"+self.userInput)
        elif self.SML==True:
            return str("True"+self.userInput)